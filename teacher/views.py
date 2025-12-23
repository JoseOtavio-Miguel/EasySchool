from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def dashboard(request):
    if request.user.role != 'teacher':
        return redirect('login')
    return render(request, 'dashboard_teacher/dashboard.html')


def teacher_create_account():
    return render(request(''))