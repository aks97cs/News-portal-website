'''
@author : Anuj kumar Singh
@desc : Models

'''

from django.db import models
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Blog(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200) # done 
	current_affairs = '0'
	politics = '1'
	sports = '2'
	culture = '3'
	business = '4'
	cat_list = (
	    (current_affairs, 'Current Affairs'),
	    (politics, 'Politics'),
	    (culture, 'Culture'),
	    (sports, 'Sports'),
	)
	category = models.CharField(
	    max_length=100,
	    choices=cat_list,
	    default=politics,
	)
	smw_img = models.FileField(upload_to='uploads/', null = True) # swm = social media widget
	smw_desc = models.CharField(max_length = 500, null = True)
	view = models.IntegerField()  # default zero  
	date = models.DateTimeField() # current date time
	title_intro = RichTextUploadingField(null=True) # done
	desc = RichTextUploadingField() # done

class PostAnalytics(models.Model):
	id = models.AutoField(primary_key = True)
	blog_id = models.CharField(max_length = 200)
	blog_title = models.CharField(max_length = 400)
	ip = models.CharField(max_length = 200)
	location = models.CharField(max_length = 200) # default null
