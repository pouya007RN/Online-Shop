from django.db import models
from datetime import datetime



class EssayCategory(models.Model):


    essay_category   = models.CharField(max_length=50)
    category_summary = models.CharField(max_length=200)
    category_Image   = models.ImageField(upload_to="IMAGES/", blank=True)
    category_slug    = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "essay category"

    def __str__(self):
        return self.essay_category



class Essay(models.Model):

    essay_title = models.CharField(max_length=200)
    essay_summary = models.CharField(max_length=200)
    essay_Image = models.ImageField(upload_to="IMAGES/%Y/%m/%d", blank=True)
    essay_category = models.ForeignKey(EssayCategory, default=1, verbose_name="category", on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "essay"

    def __str__(self):
        return self.essay_title



class EssayDetail(models.Model):
    essay_title = models.ForeignKey(Essay, default=1, verbose_name="essay", on_delete=models.SET_DEFAULT)

    essay_sidebar = models.CharField(max_length=200, default='')

    essay_demo  = models.FileField(upload_to='FILES/%Y/%m/%d',blank=True)

    essay_description = models.TextField(default="")

    essay_price = models.CharField(max_length=10,default="1,500")

    zarinpal_link = models.CharField(max_length=200, default='')

    essay_slug   = models.CharField(max_length=200, default=1)

    date = models.DateField(default=datetime.now,blank=True)




    def __str__(self):

        return str(self.essay_title)




class EssayDownload(models.Model):

    essay_title = models.ForeignKey(EssayDetail, default=1, verbose_name="essay title", on_delete=models.SET_DEFAULT)
    essay_size  = models.DecimalField(max_digits=10,decimal_places=1,default=0)
    essay_download = models.FileField(upload_to='DOWNLOADFILES/%Y/%m/%d')

    def __str__(self):
        return str(self.essay_download)




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
    post       = models.ForeignKey(EssayDetail,default=1, related_name='comments', verbose_name="comments",on_delete=models.SET_DEFAULT)
    نام       = models.CharField(max_length=250)

    دیدگاه    = models.TextField()
    timestamp  = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.نام
