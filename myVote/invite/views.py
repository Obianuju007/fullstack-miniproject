from urllib import request
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth import *
from django.contrib.auth.password_validation import validate_password

from django.contrib import messages

# Create your views here.
# 
def homepage(request):
    return render(request, 'invite/index.html')
       
def signup_view(request):
    signup_form = Signup()
    if request.method == 'POST':
        signup_form = Signup(request.POST)
        if signup_form.is_valid():  
            full_name = request.POST['full_name']
            nickname = request.POST['nickname']
            email = request.POST['email']
            gender = request.POST['gender']
            password = request.POST['password']
            # password2 = request.POST['confirm_password'] 
            user = CustomUser.objects.create_user(full_name=full_name, email=email, gender=gender, nickname=nickname, password=password)
            user = CustomUser.objects.filter(email=email).first()
            user.set_password(password)
            user.save()
            messages.success(request, 'Account successfully created!')
            return redirect('home')
    return render(request, 'invite/signup.html', {'form': signup_form})
        

def login_view(request):
    login_form = newLogin() 
    if request.method == 'POST':
        login_form = newLogin(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            messages.success(request, 'It\'s good to have you back!')
            return redirect('home')
        messages.error(request, 'Invalid login credentials!') 
        return render(request, 'invite/login.html', {'form':login_form})  
    return render(request, 'invite/login.html', {'form':login_form})
    

def Event_View(request):
    event_form = Create_Event_class()
    event_form = Create_Event_class(request.POST, request.FILES)
    print (request.FILES)
    context = {'form': event_form}
    return render(request,'invite/createevent.html', context)

# class event_print():
#     form = signup.full_name






