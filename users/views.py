from django.core.checks import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        if len(username) < 5:
            messages.info(request, 'Username Must be of 5 charecters Atleast')
        email = request.POST['email']
        password1 = request.POST.get('password', 'Guest')
        password2 = request.POST.get('password_conf', 'Guest')

        if password1 == password2:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.info(request,'Username or Email already taken')
                return redirect(reverse('users:register'))
            else:
                user = User.objects.create_user(username=username, password = password1, first_name=first_name, last_name=last_name,email=email)
                user.save()
                return redirect(reverse('users:login'))
        else:
            messages.info(request,'Passwords do not match')
            return HttpResponseRedirect(reverse('users:register'))
    else:
        return render(request, 'users/register1.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', 'Guest')
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
        else:
            messages.info(request, 'Invalid Credentials')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        return render(request, 'users/login.html')

    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))