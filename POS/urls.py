from django.urls import path
from . import views


urlpatterns = [path('', views.homepage,name="homepage"),
               path('order/',views.order_create, name="order"),
               path('<single_slug>', views.single_slug,name="single_slug"),
               ]

