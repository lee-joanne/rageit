# Generated by Django 3.2.13 on 2022-07-16 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_post_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
