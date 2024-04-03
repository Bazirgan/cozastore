from django.urls import include, path
from django.conf import settings
from core.views import  index, product, shopingcart, blog, about, contact, blog_details, search


urlpatterns = [
    path('',index, name='index'),
    path('product/',product, name='product'),
    path('shopingcart/',shopingcart, name='shopingcart'),
    path('blog/',blog, name='blog'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('blog-detail/<str:blog_slug>/', blog_details, name='blog-detail'),
    path('', include('social_django.urls', namespace='social')),
    path('search/', search, name= 'search'),
]


