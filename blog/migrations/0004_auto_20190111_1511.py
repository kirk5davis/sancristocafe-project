# Generated by Django 2.0.7 on 2019-01-11 23:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180721_0250'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='archives/')),
                ('uploaded_on', models.DateField(auto_now=True)),
                ('vintage', models.DateField(help_text='When was this file created/intended for/relevant?')),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(help_text='This will only accept PDF files!', upload_to='newsletters/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('uploaded_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Post'},
        ),
    ]
