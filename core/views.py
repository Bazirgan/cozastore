from django.shortcuts import render
from django.http import HttpResponse
from core.models import  *
from core.forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    products=Product.objects.all()
    context = {
         'products':products
     }
    
    return render(request, 'index.html',context=context)


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

    items_per_page = 7
    paginator = Paginator(products, items_per_page)
    page = request.GET.get("page")

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'products': products,
        'title': 'Product Page',
        'no_result': no_result,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'product.html', context=context)

def product_single(request, id):
    context = {
        "title": "Product Single Page",
        "product_single": Product.objects.get(id=id),
        "products": Product.objects.all().order_by("created_at"),
    }
    return render(request, "product-detail.html", context=context)


def shopingcart(request):
    context = {
        'title':'Shopingcart page',
    }
    return render(request, 'shoping-cart.html', context=context)

def blog(request):
    blogs = Blog.objects.filter(is_active=True).order_by('-created_at')
    products=Product.objects.all()
    
    items_per_page = 2
    paginator = Paginator(blogs, items_per_page)
    page = request.GET.get("page")

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
        
    context = {
        'title': Setting.objects.first().blog_title,
        'blogs': blogs, 
        'products': products,
    }
    return render(request, 'blog.html',context=context)
 
def blog_details(request, blog_slug):
    blog = Blog.objects.get(slug=blog_slug)
    products=Product.objects.all()
    context = {
        'title': blog.title,
        'products': products,
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

def about(request):
    about=About.objects.get(id=1)
    
    context = {
        'about':about
    }

    return render(request, 'about.html',context=context)

