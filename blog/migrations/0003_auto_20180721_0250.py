# Generated by Django 2.0.7 on 2018-07-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
