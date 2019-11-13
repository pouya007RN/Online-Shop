from django.contrib import admin
from .models import Order, POSCollection, POSCategory, POSDetail



class POSCatAdmin(admin.ModelAdmin):

    list_display = ['POS_category', 'category_summary']




class POSCollAdmin(admin.ModelAdmin):

    list_display = ['POS_brand','POS_summary']




class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_num',
                    #'address', 'postal_code',
                    'city',
                    'created','نام_دستگاه','paid']

    list_filter  = ['paid', 'created']


admin.site.register(Order,OrderAdmin)
admin.site.register(POSDetail)
admin.site.register(POSCategory,POSCatAdmin)
admin.site.register(POSCollection,POSCollAdmin)
