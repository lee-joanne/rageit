# Generated by Django 3.2.13 on 2022-07-05 19:42

import cloudinary.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_auto_20220705_1855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='placeholder', max_length=45),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='comment',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='blog.post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='revised_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
