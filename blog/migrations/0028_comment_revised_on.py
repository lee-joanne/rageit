# Generated by Django 3.2.13 on 2022-07-23 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_alter_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='revised_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]