# Generated by Django 3.2.13 on 2022-07-23 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_alter_post_revised_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='revised_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]