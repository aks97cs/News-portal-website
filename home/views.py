from django.shortcuts import render
from django.http import HttpResponse
from home.models import Blog
from config.define import Constant
from django.core.paginator import Paginator
# Home Page
def index(request):
	b_data = Blog.objects.order_by('-date',)
	popular_post = Blog.objects.order_by('-view',)[0:5]
	print(b_data[0].title)
	d_blog = 0
	paginator = Paginator(b_data, 5)
	page = request.GET.get('page')
	post_data = paginator.get_page(page)
	is_mobile = request.user_agent.is_mobile
	print(is_mobile)
	return render(request, 'home/index.html',{
			'b_data' : post_data,
			'popular_post' : popular_post,
			'd_blog' : d_blog,
			'is_mobile' : is_mobile
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
	catg = b_data[0].category
	t_data = c.category
	is_mobile = request.user_agent.is_mobile
	return render(request, 'home/blog_details.html',{
			'b_data' : b_data[0],
			'popular_post' : popular_post,
			'recent_post' : recent_post,
			'catg' : t_data[catg],
			'url' : uri,
			'ip' : ip,
			'd_blog' : 1,
			'is_mobile' : is_mobile

		})

# Function for catecory wise post
def post_by_catg(request, catg):
	c = Constant()
	b_data = Blog.objects.filter(category = catg)
	popular_post = Blog.objects.order_by('-view')[0:5]
	recent_post = Blog.objects.order_by('-date')[0:5]
	is_mobile = request.user_agent.is_mobile
	return render(request, 'home/blog_via_category.html',{
		'b_data' : b_data,
		'popular_post' : popular_post,
		'recent_post' : recent_post,
		'catg' : c.category[catg],
		'd_blog' : 0,
		'is_mobile' : is_mobile

	})

# Function to get client ip and update on db

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip
