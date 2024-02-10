from django.urls import path
from django.conf.urls import include

from core.views import  index, product, shopingcart, blog, about, contact

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('index/',index, name='index'),
    path('product/',product, name='product'),
    path('shopingcart/',shopingcart, name='shopingcart'),
    path('blog/',blog, name='blog'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
]


