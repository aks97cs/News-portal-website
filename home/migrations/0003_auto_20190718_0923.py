# Generated by Django 2.2.3 on 2019-07-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_postanalytics'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='smw_desc',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='smw_img',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]
