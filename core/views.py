from django.shortcuts import render
from django.http import HttpResponse
from core.models import Blog, Contact, Product, Setting
from core.forms import ContactForm

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def product(request):
    context = {
        'products':Product.objects.all(),
        'title':'product page'
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
        'title':Setting.objects.get(id=1).blog_title,
        'blogs': blogs, 
        'blog_count': blogs.count()
    }
    return render(request, 'blog.html',context=context)
 
def blog_details(request, blog_slug):
    blog = Blog.objects.get(slug=blog_slug)
    context = {
        'title': blog.title,
        'blog': blog
    }
    return render(request, 'blog-detail.html', context=context)

def about(request):
    context = {
        'title':'about page',
    }
    return render(request, 'about.html',context=context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', context={'contact_form': ContactForm()})
    contacts = Contact.objects.filter(is_active=True).order_by('-created_at') 
    context = {
        'contact_form': ContactForm(),
        'title': 'Contact page',
        'contact': contacts.first()
    }
    return render(request, 'contact.html',context=context)


