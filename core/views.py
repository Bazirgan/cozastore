from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def product(request):
    
    return render(request, 'product.html')

def shopingcart(request):
    
    return render(request, 'shoping-cart.html')

def blog(request):
    
    return render(request, 'blog.html') 

def about(request):
    
    return render(request, 'about.html')

def contact(request):
    
    return render(request, 'contact.html')