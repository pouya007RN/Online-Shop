from django.contrib import admin

from .models import Essay, EssayDownload, EssayDetail, EssayCategory, Order, Comment

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['essay_category', 'category_summary']

class DetailAdmin(admin.ModelAdmin):

    list_display = ['essay_title','essay_sidebar']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'نام', 'نام_خانوادگی', 'آدرس_ایمیل', 'شماره_تماس',
                    #'address', 'postal_code',

                    'created', 'paid']

    list_filter  = ['paid', 'created']


class CommentAdmin(admin.ModelAdmin):

    list_display = ['post' ,'نام','دیدگاه','timestamp']



admin.site.register(EssayCategory,CategoryAdmin)

admin.site.register(Essay)

admin.site.register(EssayDetail,DetailAdmin)

admin.site.register(EssayDownload)

admin.site.register(Order,OrderAdmin)

admin.site.register(Comment,CommentAdmin)
