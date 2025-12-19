from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            messages.success(
                request,
                f'Bem-vindo, {user.first_name}!'
            )

            if user.role == 'student':
                return redirect('student:dashboard')
            elif user.role == 'teacher':
                return redirect('teacher:dashboard')
            elif user.role == 'admin':
                return redirect('administrator:dashboard')
            else:
                return redirect('/')

        # login inválido
        messages.error(request, 'Usuário ou senha inválidos')

    return render(request, 'login/login_content.html')


