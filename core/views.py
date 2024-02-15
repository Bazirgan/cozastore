from django.shortcuts import render
from django.http import HttpResponse
from core.models import Blog, ContactUs

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def product(request):
    context = {
        'title':'product page',
    }
    return render(request, 'product.html', context=context)

def shopingcart(request):
    context = {
        'title':'Shopingcart page',
    }
    return render(request, 'shoping-cart.html', context=context)

def blog(request):
    blogs = Blog.objects.filter(is_active=True).order_by('-created_at')
    context = {
        'title':'Blog page',
        'blogs': blogs, 
        'blog_count': blogs.count()
    }
    return render(request, 'blog.html',context=context)
 

def about(request):
    context = {
        'title':'about page',
    }
    return render(request, 'about.html',context=context)

def contact(request):
    contact = ContactUs.objects.filter(is_active=True).order_by('-created_at') 
    context = {
        'contact': contact,
        'title': 'Contact page'   
    }
    return render(request, 'contact.html',context=context)


