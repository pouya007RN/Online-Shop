"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('sarga98/', admin.site.urls),
    path('videos/', include('video.urls')),
    path('POS-device/', include('POS.urls')),
    path('essay/', include('essay.urls')),
    path('',include('home.urls')),
    url(r'^cart/', include(('cart.urls','cart'), namespace='cart')),
    url(r'^order/', include(('orders.urls','orders'), namespace='orders')),
   # url(r'^payment/', include(('payment.urls','payment'), namespace='payment')),
    url(r'^shop/',include(('shop.urls', 'shop'), namespace='shop'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
