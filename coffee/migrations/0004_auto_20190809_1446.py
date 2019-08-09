# Generated by Django 2.1.5 on 2019-08-09 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0003_coffee_origin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='coffee',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='coffee',
            name='origin_info',
        ),
        migrations.AlterField(
            model_name='coffee',
            name='description',
            field=models.TextField(help_text='Write out exactly how you would like it to show on the coffee tile!'),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]