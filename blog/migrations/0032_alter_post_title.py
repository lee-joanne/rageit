# Generated by Django 3.2.13 on 2022-07-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_alter_post_revised_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
