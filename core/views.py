from django.shortcuts import render
from django.http import HttpResponse
from core.models import Blog, ContactUs

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def product(request):
    
    return render(request, 'product.html')

def shopingcart(request):
    
    return render(request, 'shoping-cart.html')

def blog(request):
    context = {
        'blogs': Blog.objects.all()   
    }
    return render(request, 'blog.html',context=context)
 

def about(request):
    
    return render(request, 'about.html')

def contact(request):
    
    context = {
        'contact': ContactUs.objects.filter(is_active=True).order_by('-created_at')    
    }
    return render(request, 'contact.html',context=context)


