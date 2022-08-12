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
        full_name = request.POST['full_name']
        nickname = request.POST['nickname']
        email = request.POST['email']
        gender = request.POST['gender_select']
        password = request.POST['password']
        account = CustomUserManager.objects.create_user(
            full_name = full_name,
            email = email,
            gender = gender,
            password=password,
        )   
        return render(request, 'invite/signup.html', {'form': account})
        # signup_form = Signup(request.POST) 
    #     if signup_form.is_valid():
    #         # signup_form.save(commit=False)
    #         password = signup_form.cleaned_data['password']
    #         password2 = signup_form.cleaned_data['confirm_password']
    #         email = signup_form.cleaned_data['email']
    #         if password!= password2:
    #             messages.error(request, 'Passwords don\'t match')
    #             return redirect('signup')
    #         elif Signup.object.get(email = email).exists():
    #             messages.error(request, 'Email already exists, try signing in!')
    #             return redirect('signup')
    #         else:
    #             signup_form.save()
    #             user = Signup.object.get(email=signup_form.cleaned_data['email'])
    #             user.set_password(password)
    #             user.save()
    #             messages.success(request, 'Account successfully created!')
            # return redirect('home')
    # return render(request, 'invite/signup.html', {'form': signup_form})
    # return render(request, 'invite/signup.html', {'form': signup_form})
        

def login_view(request):
    login_form = login() 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, 'It\'s good to have you back!')
            return redirect('home')
        messages.error(request, 'Invalid login credentials!')   
    return render(request, 'invite/login.html', {'form':login_form})
    

def Event_View(request):
    event_form = Create_Event_class()
    event_form = Create_Event_class(request.POST, request.FILES)
    print (request.FILES)
    context = {'form': event_form}
    return render(request,'invite/createevent.html', context)

# class event_print():
#     form = signup.full_name






