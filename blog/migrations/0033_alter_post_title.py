# Generated by Django 3.2.13 on 2022-07-24 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]