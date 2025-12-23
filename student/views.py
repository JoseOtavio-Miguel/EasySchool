from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from student.models import Student
from accounts.models import User


@login_required
def dashboard(request):
    if request.user.role != 'student':
        return redirect('login')
    return render(request, 'dashboard_student/dashboard.html')


# Create your views here.
def index(request):
    return render(request, 'homepage.html')
from django.db import transaction


@transaction.atomic
def student_create_account(request):
    if request.method == "POST":
        try:
            student = Student.objects.create(
                first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
                cpf=request.POST.get("cpf"),
                rg=request.POST.get("rg"),
                date_of_birth=request.POST.get("date_of_birth"),
                gender=request.POST.get("gender"),
                enrollment_number=request.POST.get("enrollment_number"),
                grade_level=request.POST.get("grade_level"),
                specific_grade=request.POST.get("specific_grade"),
                shift=request.POST.get("shift"),
                father_name=request.POST.get("father_name"),
                mother_name=request.POST.get("mother_name"),
                guardian_name=request.POST.get("guardian_name"),
                email=request.POST.get("email"),
                phone=request.POST.get("phone"),
                guardian_phone=request.POST.get("guardian_phone"),
                address=request.POST.get("address"),
                address_number=request.POST.get("address_number"),
                complement=request.POST.get("complement"),
                neighborhood=request.POST.get("neighborhood"),
                zip_code=request.POST.get("zip_code"),
                city=request.POST.get("city"),
                state=request.POST.get("state"),
            )

            cpf_clean = student.cpf.replace(".", "").replace("-", "")
            email = student.email

            User.objects.create_user(
                username=email,
                email=email,
                password=cpf_clean,
                role="student",
                student=student
            )

            messages.success(request, "Estudante e login criados com sucesso!")
            return redirect("students:list")

        except Exception as e:
            messages.error(request, f"Erro ao cadastrar estudante: {e}")

    return render(request, "dashboard_admin/dashboard.html")
