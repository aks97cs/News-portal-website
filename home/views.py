from django.shortcuts import render
from django.http import HttpResponse
from home.models import Blog
from config.define import Constant

# Home Page
def index(request):
	b_data = Blog.objects.all()
	popular_post = Blog.objects.order_by('-view',)[0:5]
	print(b_data[0].title)
	return render(request, 'home/index.html',{
			'b_data' : b_data,
			'popular_post' : popular_post
		})

# Function for blog details
def blog_details(request, id = 1):
	c = Constant()
	b_data = Blog.objects.filter(id = id)
	popular_post = Blog.objects.order_by('-view')[0:5]
	recent_post = Blog.objects.order_by('-date')[0:5]
	url = request.get_full_path()
	uri = "http://thedailyreport.co.in"+str(url)
	return render(request, 'home/blog_details.html',{
			'b_data' : b_data[0],
			'popular_post' : popular_post,
			'recent_post' : recent_post,
			'catg' : c.category,
			'url' : uri
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
		'catg' : c.category[catg]
	})

