# Generated by Django 3.2.13 on 2022-07-13 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_comment_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
    ]