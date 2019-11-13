from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^downloaded/Acdr458330100/$', views.download, name='download')
]