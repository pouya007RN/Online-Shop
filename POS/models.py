from django.db import models
from datetime import datetime



class POSCategory(models.Model):


    POS_category   = models.CharField(max_length=50)
    category_summary = models.CharField(max_length=200)
    category_Image   = models.ImageField(upload_to="IMAGES/POS/", blank=True)
    category_slug    = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "POS category"

    def __str__(self):
        return self.POS_category



class POSCollection(models.Model):

    POS_brand = models.CharField(max_length=200)
    POS_summary = models.CharField(max_length=200)
    POS_Image = models.ImageField(upload_to="IMAGES/POS/%Y/%m/%d", blank=True)
    POS_category = models.ForeignKey(POSCategory, default=1, verbose_name="POS category", on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "POS coll"

    def __str__(self):
        return self.POS_brand



class POSDetail(models.Model):

    POS_brand = models.ForeignKey(POSCollection, default=1, verbose_name="POS brand", on_delete=models.SET_DEFAULT)

    POS_Image  = models.ImageField(upload_to='IMAGES/POS/%Y/%m/%d',blank=True)

    POS_description = models.TextField(default="")

    POS_price = models.CharField(max_length=10,default="توافقی")

    POS_slug   = models.CharField(max_length=200, default=1)

    date = models.DateField(default=datetime.now,blank=True)




    def __str__(self):

        return str(self.POS_brand)
    


class Order(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    email       = models.EmailField()
    phone_num   = models.CharField(max_length=15, default='09')
    city        = models.CharField(max_length=100)
    نام_دستگاه  = models.ForeignKey(POSDetail, default=1,on_delete=models.SET_DEFAULT)
    created     = models.DateTimeField(auto_now_add=True)
    paid        = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)
