from django.contrib import admin

from .models import VideoCategory, VideoDetail, Videos, VideoDownload, Order, Comment

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['video_category', 'category_summary']

class DetailAdmin(admin.ModelAdmin):

    list_display = ['video_title','video_sidebar']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'نام', 'نام_خانوادگی', 'آدرس_ایمیل', 'شماره_تماس',
                    #'address', 'postal_code',

                    'created', 'paid']

    list_filter  = ['paid', 'created']

class CommentAdmin(admin.ModelAdmin):

    list_display = ['post' ,'نام','دیدگاه', 'timestamp']


admin.site.register(VideoCategory,CategoryAdmin)

admin.site.register(Videos)

admin.site.register(VideoDetail,DetailAdmin)

admin.site.register(VideoDownload)

admin.site.register(Order,OrderAdmin)

admin.site.register(Comment,CommentAdmin)