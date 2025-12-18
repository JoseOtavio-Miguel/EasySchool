from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'public/homepage.html')


# Login Page
def login_page(request):
    return render(request, 'login/login_content.html')