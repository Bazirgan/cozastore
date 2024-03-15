from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RegisterForm, LoginForm


def register(request):
    form = RegisterForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        if request.POST['password'] != request.POST['confirm_password']:
            context['error'] = 'Passwords do not match'
            return render(request, 'register.html', context)
        else:
            form = RegisterForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                user.set_password(user.password)
                user.save()
                return redirect('index')
    return render(request, 'register.html', context)


def login(request):
    context = {
        'title':'Login',
        'form':LoginForm()
    }
    if request.method == 'POST':
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth_login(request,user)
            return redirect('index')
        else:
            context['error'] = 'Invalid Username of Password'
            
    return render(request,'login.html',context)




