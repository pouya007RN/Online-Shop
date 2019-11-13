from django.db import models
from datetime import datetime



class VideoCategory(models.Model):


    video_category   = models.CharField(max_length=50)
    category_summary = models.CharField(max_length=200)
    category_Image   = models.ImageField(upload_to="IMAGES/", blank=True)
    category_slug    = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "video category"

    def __str__(self):
        return self.video_category



class Videos(models.Model):

    video_title = models.CharField(max_length=200)
    video_summary = models.CharField(max_length=200)
    video_Image = models.ImageField(upload_to="IMAGES/%Y/%m/%d", blank=True)
    video_category = models.ForeignKey(VideoCategory, default=1, verbose_name="category", on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "videos"

    def __str__(self):
        return self.video_title



class VideoDetail(models.Model):

    video_title = models.ForeignKey(Videos, default=1, verbose_name="Videos", on_delete=models.SET_DEFAULT)

    video_name  = models.CharField(max_length=50, default='')

    video_sidebar = models.CharField(max_length=200, default='')

    video_demo  = models.FileField(upload_to='CLIPS/%Y/%m/%d',blank=True)

    video_description = models.TextField(default="")

    video_size = models.DecimalField(max_digits=10, decimal_places=1, default=0)

    video_price = models.CharField(max_length=10,default="5,000")

    zarinpal_link = models.CharField(max_length=200, default='')

    video_slug   = models.CharField(max_length=200, default=1)

    date = models.DateField(default=datetime.now,blank=True)




    def __str__(self):

        return str(self.video_name)


class VideoDownload(models.Model):

    video_title = models.ForeignKey(VideoDetail, default=1, verbose_name="Video title", on_delete=models.SET_DEFAULT)

    video_download = models.FileField(upload_to='DOWNLOADCLIPS/%Y/%m/%d')

    def __str__(self):
        return str(self.video_download)




class Order(models.Model):

    نام  = models.CharField(max_length=50)
    نام_خانوادگی   = models.CharField(max_length=50)
    آدرس_ایمیل       = models.EmailField(blank=True)
    شماره_تماس   = models.CharField(max_length=15, default='09')
    created     = models.DateTimeField(auto_now_add=True)
    paid        = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)


class Comment(models.Model):
    post       = models.ForeignKey(VideoDetail,default=1, related_name='comments', verbose_name="comments",on_delete=models.SET_DEFAULT)
    نام       = models.CharField(max_length=250)

    دیدگاه    = models.TextField()
    timestamp  = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.نام
