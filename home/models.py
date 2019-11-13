from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Contact(models.Model):

    نام = models.CharField(max_length=50)

    نام_خانوادگی = models.CharField(max_length=50, verbose_name='نام خانوادگی')

    ایمیل = models.EmailField()

    شماره_تماس = models.CharField(max_length=15, default='09', verbose_name='شماره تماس')

    موضوع = models.CharField(max_length=50)

    پیام_شما = models.TextField()


    def __str__(self):

        return self.نام



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

