from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'public/homepage.html')


# Login Page
def login_page(request):
    return render(request, 'login/login_content.html')


