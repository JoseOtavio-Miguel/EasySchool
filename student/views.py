from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from student.models import Student
from django.contrib import messages


@login_required

def dashboard(request):
    if request.user.role != 'student': # Redirect to login if user is not a student
        return redirect('login')
    return render(request, 'dashboard_student/dashboard.html')


def index(request):
    return render(request, 'homepage.html')


# Process the student registration form
def student_create_account(request):
    if request.method == "POST":
        try:
            Student.objects.create(
                # Personal Data
                first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
                cpf=request.POST.get("cpf"),
                rg=request.POST.get("rg"),
                date_of_birth=request.POST.get("date_of_birth"),
                gender=request.POST.get("gender"),

                # Schoolar information
                enrollment_number=request.POST.get("enrollment_number"),
                grade_level=request.POST.get("grade_level"),
                specific_grade=request.POST.get("specific_grade"),
                shift=request.POST.get("shift"),

                # Parents information
                father_name=request.POST.get("father_name"),
                mother_name=request.POST.get("mother_name"),
                guardian_name=request.POST.get("guardian_name"),

                # Contact information
                email=request.POST.get("email"),
                phone=request.POST.get("phone"),
                guardian_phone=request.POST.get("guardian_phone"),

                # Address information
                address=request.POST.get("address"),
                address_number=request.POST.get("address_number"),
                complement=request.POST.get("complement"),
                neighborhood=request.POST.get("neighborhood"),
                zip_code=request.POST.get("zip_code"),
                city=request.POST.get("city"),
                state=request.POST.get("state"),
            )
            messages.success(" Estudante cadastrado com sucesso !")

        except Exception as e:
            messages.error(request, f' Erro ao cadastrar estudante \n Informação do erro: {e}')   

    return render(request, "dashboard_admin/dashboard.html")
