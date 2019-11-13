from django.shortcuts import render, redirect
from POS.models import POSCategory, POSCollection, POSDetail
from video.models import VideoCategory
from video.views import download_link
from essay.models import EssayCategory
from essay.views import download_link_es
from django.contrib.auth import login,logout, authenticate
from . import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm

def homepage(request):
    download_link.clear()
    download_link_es.clear()

    POS   = POSCategory.objects.all()
    video = VideoCategory.objects.all()
    POS_Coll = POSCollection.objects.all()
    POS_det  = POSDetail.objects.all()
    essay = EssayCategory.objects.all()



    return render(request, 'home/index.html',{'POS':POS_Coll,
                                              'POS_cat':POS,
                                              'POS_det':POS_det,
                                              'video':video,
                                              'essay':essay})


def loginPage(request):
    uservalue = ''
    passwordvalue = ''

    form = forms.Loginform(request.POST or None)
    if form.is_valid():
        uservalue = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")

        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            global is_authenticated
            is_authenticated = True
            context = {'form': form,
                       'error': 'The login has been successful'}

            return render(request, 'home/index.html', context)
        else:
            context = {'form': form,
                       'error': 'The username and password combination is incorrect'}

            return render(request, 'home/login.html', context)

    else:
        context = {'form': form}
        return render(request, 'home/login.html', context)


@login_required
def logout_request(request):
    logout(request)
    global is_authenticated
    is_authenticated = False
    return redirect("/")


def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('success/')
    else:
        form = forms.SignUpForm()
    return render(request, 'home/signup.html', {'form': form})

@login_required
def Loading(request):

    return render(request, 'home/Loading.html')



def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST or None)

        if contact_form.is_valid():
            name = request.POST.get('نام')
            last_name = request.POST.get('نام_خانوادگی')
            email = request.POST.get('ایمیل')
            phone = request.POST.get('شماره_تماس')
            issue = request.POST.get('موضوع')
            mail  = request.POST.get('پیام_شما')

            user_mail = Contact.objects.create( نام=name, نام_خانوادگی=last_name, ایمیل=email, شماره_تماس=phone,
                                              موضوع=issue, پیام_شما=mail)
            user_mail.save()
            return HttpResponseRedirect("/")

    else:
        contact_form = ContactForm()

    return render(request, 'home/contact.html', {'Con_form':contact_form})