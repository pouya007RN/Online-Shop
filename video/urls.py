from django.urls import path
from . import views


urlpatterns = [path('', views.homepage,name="homepage"),
               path('canceled/',views.canceled, name="canceled"),
               path('place-order/',views.order_create, name="order"),
               path('<url_generator>/link/<link>', views.link, name='link'),
               path('<single_slug>', views.single_slug,name="single_slug"),

               ]

