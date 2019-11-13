# Generated by Django 2.2.3 on 2019-09-18 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20190918_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='videodetail',
            name='video_download',
            field=models.FileField(blank=True, upload_to='DOWNLOADCLIPS/%Y/%m/%d"'),
        ),
        migrations.AlterField(
            model_name='videodetail',
            name='video_demo',
            field=models.FileField(blank=True, upload_to='CLIPS/%Y/%m/%d"'),
        ),
    ]
