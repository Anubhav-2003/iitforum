from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
    if request.user.is_authenticated == True:
        return render(request, 'main/index.html')
    else: 
        return HttpResponseRedirect(reverse('users:login'))


