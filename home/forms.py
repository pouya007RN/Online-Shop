from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact

class SignUpForm(UserCreationForm):
    Email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'Email', 'password1', 'password2', )


class Loginform(forms.Form):
    username= forms.CharField(max_length= 25,label="Enter username")
    password= forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)



class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact

        fields = ('نام', 'نام_خانوادگی', 'ایمیل', 'شماره_تماس','موضوع','پیام_شما',)
