# Generated by Django 2.2.3 on 2019-09-18 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_auto_20190918_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videodetail',
            name='video_download',
        ),
        migrations.CreateModel(
            name='VideoDownload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_download', models.FileField(blank=True, upload_to='DOWNLOADCLIPS/%Y/%m/%d')),
                ('video_title', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='video.VideoDetail', verbose_name='Video title')),
            ],
        ),
    ]
