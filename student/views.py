from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    if request.user.role != 'student':
        return redirect('login')
    return render(request, 'dashboard_student/dashboard.html')


# Create your views here.
def index(request):
    return render(request, 'homepage.html')