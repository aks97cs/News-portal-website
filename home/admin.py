from django.contrib import admin
from home.models import Blog, PostAnalytics
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = ['title']
admin.site.register(Blog, BlogAdmin)

class PostAnalyticsAdmin(admin.ModelAdmin):
	list_display = ['ip']
admin.site.register(PostAnalytics, PostAnalyticsAdmin) 
