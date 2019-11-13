from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):

    list_display = ['نام', 'نام_خانوادگی', 'شماره_تماس', 'موضوع', 'پیام_شما']

admin.site.register(Contact,ContactAdmin)