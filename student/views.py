from django.shortcuts import render, redirect,  get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from student.models import Student
from accounts.models import User
from django.db import transaction


app_name = "student"

@login_required
def dashboard(request):
    if request.user.role != 'student':
        return redirect('login')
    return render(request, 'dashboard_student/dashboard.html')


# Create your views here.
def index(request):
    return render(request, 'homepage.html')


@transaction.atomic
def student_create_account(request):
    students = Student.objects.all()
    student_id = students.lenght() + 1
 

    if request.method == "POST":
        try:
            student = Student.objects.create(
                first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
                cpf=request.POST.get("cpf"),
                rg=request.POST.get("rg"),
                date_of_birth=request.POST.get("date_of_birth"),
                gender=request.POST.get("gender"),
                enrollment_number= student.id.zfill(5),
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

            context = {
                "is_edit": False,
                "form_action": reverse("student:student_create_account"),
                "student": None,
                'open_student_modal': False,
            }

            messages.success(request, "Estudante e login criados com sucesso!")
            return redirect("administrator:list_students")

        except Exception as e:
            print("ERRO AO CRIAR ESTUDANTE:", e)
            messages.error(request, f"Erro ao cadastrar estudante: {e}")


    return render(request, "administrator:list_teachers", context)



@transaction.atomic
def student_edit_account(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        try:
            student.first_name = request.POST.get("first_name")
            student.last_name = request.POST.get("last_name")
            student.cpf = request.POST.get("cpf")
            student.rg = request.POST.get("rg")
            student.date_of_birth = request.POST.get("date_of_birth")
            student.gender = request.POST.get("gender")
            student.grade_level = request.POST.get("grade_level")
            student.specific_grade = request.POST.get("specific_grade")
            student.shift = request.POST.get("shift")
            student.father_name = request.POST.get("father_name")
            student.mother_name = request.POST.get("mother_name")
            student.guardian_name = request.POST.get("guardian_name")
            student.email = request.POST.get("email")
            student.phone = request.POST.get("phone")
            student.guardian_phone = request.POST.get("guardian_phone")
            student.address = request.POST.get("address")
            student.address_number = request.POST.get("address_number")
            student.complement = request.POST.get("complement")
            student.neighborhood = request.POST.get("neighborhood")
            student.zip_code = request.POST.get("zip_code")
            student.city = request.POST.get("city")
            student.state = request.POST.get("state")

            student.save()

            messages.success(request, "Dados do estudante atualizados com sucesso!")
            return redirect("administrator:list_students")

        except Exception as e:
            print("ERRO AO EDITAR ESTUDANTE:", e)
            messages.error(request, f"Erro ao atualizar estudante: {e}")

    # GET → exibir formulário preenchido
    context = {
        'student': student,
        'page': 'list_students',
        'open_student_modal': False,

        "is_edit": True,
        "form_action": reverse("student:student_edit_account", args=[student.id]),
        "student": student,
    }

    return render(request, "dashboard_admin/dashboard.html", context)
