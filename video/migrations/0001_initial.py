# Generated by Django 2.2.3 on 2019-09-17 21:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_category', models.CharField(max_length=50)),
                ('category_summary', models.CharField(max_length=200)),
                ('category_Image', models.ImageField(blank=True, upload_to='IMAGES/')),
                ('category_slug', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'video category',
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=200)),
                ('video_summary', models.CharField(max_length=200)),
                ('video_Image', models.ImageField(blank=True, upload_to='IMAGES/')),
                ('video_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='video.VideoCategory', verbose_name='category')),
            ],
            options={
                'verbose_name_plural': 'videos',
            },
        ),
        migrations.CreateModel(
            name='VideoDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_demo', models.FileField(blank=True, upload_to='CLIPS/')),
                ('video_description', models.TextField(default='')),
                ('video_price', models.CharField(default='5000', max_length=10)),
                ('video_slug', models.CharField(default=1, max_length=200)),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('video_title', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='video.Videos', verbose_name='Videos')),
            ],
        ),
    ]
