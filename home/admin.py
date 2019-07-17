from django.contrib import admin
from home.models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = ['title']
admin.site.register(Blog, BlogAdmin)