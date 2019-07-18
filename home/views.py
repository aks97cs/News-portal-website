from django.shortcuts import render
from django.http import HttpResponse
from home.models import Blog
from config.define import Constant

# Home Page
def index(request):
	b_data = Blog.objects.all()
	popular_post = Blog.objects.order_by('-view',)[0:5]
	print(b_data[0].title)
	d_blog = 0
	return render(request, 'home/index.html',{
			'b_data' : b_data,
			'popular_post' : popular_post,
			'd_blog' : d_blog
		})

# Function for blog details
def blog_details(request, id = 1):
	c = Constant()
	b_data = Blog.objects.filter(id = id)
	popular_post = Blog.objects.order_by('-view')[0:5]
	recent_post = Blog.objects.order_by('-date')[0:5]
	url = request.get_full_path()
	uri = "http://thedailyreport.co.in"+str(url)
	ip = get_client_ip(request)
	b_view = int(b_data[0].view)+1
	#return HttpResponse(b_view)
	Blog.objects.filter(id = id).update(view = b_view)
	return render(request, 'home/blog_details.html',{
			'b_data' : b_data[0],
			'popular_post' : popular_post,
			'recent_post' : recent_post,
			'catg' : c.category,
			'url' : uri,
			'ip' : ip,
			'd_blog' : 1
		})

# Function for catecory wise post
def post_by_catg(request, catg):
	c = Constant()
	b_data = Blog.objects.filter(category = catg)
	popular_post = Blog.objects.order_by('-view')[0:5]
	recent_post = Blog.objects.order_by('-date')[0:5]
	return render(request, 'home/blog_via_category.html',{
		'b_data' : b_data,
		'popular_post' : popular_post,
		'recent_post' : recent_post,
		'catg' : c.category[catg],
		'd_blog' : 0
	})

# Function to get client ip and update on db

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip
