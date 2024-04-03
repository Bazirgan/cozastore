from django.shortcuts import render
from django.http import HttpResponse
from core.models import  Blog, Contact, Product, Setting
from core.forms import ContactForm

# Create your views here.

def index(request):
    
    return render(request, 'index.html')


def product(request):
    from django.db.models import Q  
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    
    start_date = None
    end_date = None
    
    if request.method == 'POST':
        user_input = request.POST.get('product_search')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        if user_input:
            products = products.filter(name__icontains=user_input)
        if start_date and end_date:
            products = products.filter(
                Q(created_at__date__gte=start_date),
                Q(created_at__date__lte=end_date)
            )
    if len(products) == 0:
        no_result = 'Product tapılmadı'
    else:
        no_result = None
    context = {
        'products': products,
        'title': 'Product Page',
        'no_result': no_result,
        'start_date': start_date,
        'end_date': end_date,
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
        'title': Setting.objects.first().blog_title,
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


def search(request):
    blogs = Blog()
    products = Product()
    if request.method == 'POST':
        user_input = request.POST.get('search')
        print('user_input: ', user_input)
        blogs = Blog.objects.filter(title__icontains=user_input)
        products = Product.objects.filter(name__icontains=user_input)
        
        
        context = {
            'title': 'search',
            'blogs': blogs,
            'products': products, 
        }
        
        return render(request, 'search.html', context=context)
    
    return render (request,'search.html')
