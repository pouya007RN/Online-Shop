# Generated by Django 3.0.6 on 2020-08-24 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('نام', models.CharField(max_length=50)),
                ('نام_خانوادگی', models.CharField(max_length=50, verbose_name='نام خانوادگی')),
                ('ایمیل', models.EmailField(max_length=254)),
                ('شماره_تماس', models.CharField(default='09', max_length=15, verbose_name='شماره تماس')),
                ('موضوع', models.CharField(max_length=50)),
                ('پیام_شما', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
