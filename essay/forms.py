from django import forms
from .models import Order, Comment

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['نام', 'نام_خانوادگی', 'آدرس_ایمیل', 'شماره_تماس']#, 'city']#, 'address', 'postal_code',]



class CommentForm(forms.ModelForm):
    class Meta:
        model  = Comment
        fields = ('نام','دیدگاه',)
