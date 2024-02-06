from django.urls import path
from core.views import index, product, shopingcart, blog, about, contact

urlpatterns = [
    path('index.html', index, name='index'),
    path('product', product, name='product'),
    path('shoping-cart.html', shopingcart, name='shopingcart'),
    path('blog.html', blog, name='blog'),
    path('about.html', about, name='about'),
    path('contact.html', contact, name='contact')
]


