from django.urls import path
from . import views


urlpatterns = [path('', views.homepage,name="homepage"),
               path('contact/', views.contact, name='contact'),
               path('login/' ,views.loginPage, name = 'login'),
               path('signup/' ,views.signup, name='signup'),
               path('logout/', views.logout_request, name='logout'),
               path('signup/success/',views.Loading, name='Loading'),

               ]