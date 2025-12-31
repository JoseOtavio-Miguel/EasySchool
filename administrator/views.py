from django.shortcuts import render, redirect, get_object_or_404    
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from django.db import transaction
from django.contrib import messages


from student.models import Student
from teacher.models import Teacher
from administrator.forms import StudentForm  


# Create your views here.
@login_required
def dashboard(request):
    if request.user.role != 'admin':
        return redirect('login')
    return render(request, 'dashboard_admin/dashboard.html')

from django.db.models import Q


def list_students(request):
    students = Student.objects.all()

    q = request.GET.get('q')
    level = request.GET.get('level')

    if q:
        students = students.filter(
            Q(first_name__icontains=q) |
            Q(last_name__icontains=q) |
            Q(email__icontains=q) |
            Q(enrollment_number__icontains=q)
        )

    if level:
        students = students.filter(grade_level=level)

    context = {
        'students': students,
        'page': 'list_students',
        'open_student_modal': request.session.pop('open_student_modal', False),
    }

    return render(request, 'dashboard_admin/dashboard.html', context)



def list_teachers(request):
    teachers = Teacher.objects.all()

    context = {
        'teachers': teachers,
        'page': 'list_teachers',
        'open_teacher_modal': request.session.pop('open_teacher_modal', False),
    }

    return render(request, 'dashboard_admin/dashboard.html', context)



def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno atualizado com sucesso!')
            return redirect('administrator:list_students') 
    else:
        form = StudentForm(instance=student)
    
    context = {
        'form': form,
        'student': student,
        'page': 'edit_student',
    }
    return render(request, 'dashboard_admin/edit_student.html', context)


def deactivate_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        student.is_active = False
        student.save()
        messages.success(request, f'Aluno {student.name} desativado com sucesso!')
    
    return redirect('administrator:list_students')  


def deactivate_teacher(request, student_id):
    if request.method == 'POST':
        teacher = get_object_or_404(Student, id=student_id)
        teacher.is_active = False
        teacher.save()
        messages.success(request, f'Professor {teacher.name} desativado com sucesso!')
    
    return redirect('administrator:list_teacher')  


"""
def openModal_create(request):
    students = Student.objects.all()
    enrollment = str(students.count() + 1).zfill(4)

    context = {
        'students': students,
        'enrollment': enrollment,
        'open_student_modal': True,
        'page': 'list_students',
    }

    return render(request, 'dashboard_admin/dashboard.html', context)
"""

def openModal_create_teacher(request):
    teachers = Teacher.objects.all()

    context = {
        'teachers': teachers,
        'open_teacher_modal': True,
        'page': 'list_teachers',
    }

    return render(request, 'dashboard_admin/dashboard.html', context)


def openModal_edit_teacher(request, student_id):
    teachers = Teacher.objects.all()
    teacher = get_object_or_404(Teacher, id=student_id)

    context = {
        'teachers': teachers,
        'teacher': teacher,
        'open_teacher_modal': True,
        'page': 'list_teacher',

        "is_edit": True,
        "form_action": reverse("administrator:teacher_edit_account", args=[teacher.id]),
        "teacher": teacher,
    }

    return render(request, 'dashboard_admin/dashboard.html', context)


def openModal_edit(request, student_id):
    students = Student.objects.all()
    student = get_object_or_404(Student, id=student_id)

    context = {
        'students': students,
        'student': student,
        'open_student_modal': True,
        'page': 'list_students',

        "is_edit": True,
        "form_action": reverse("student:student_edit_account", args=[student.id]),
        "student": student,
    }

    return render(request, 'dashboard_admin/dashboard.html', context)   

def closeModal(request):
    students = Student.objects.all() 
    student = get_object_or_404(Student, id=student_id)

    context = {
        'open_student_modal': False,
        'student_id': student_id,
        'students': students,
        'student': student,
        'page': 'list_students',
    }

    return render(request, 'dashboard_admin/dashboard.html', context)



# Register Teacher account on DataBase 
@transaction.atomic
def teacher_create_account(request):
    teachers = Teacher.objects.all()
    teacher = None
    teacher_id = teachers.count() + 1
    trasaction = ''
 

    if request.method == "POST":
        try:
            transaction = 'create'

            teacher = Teacher.objects.create(
                # Personal Data [User]
                first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
                cpf=request.POST.get("cpf"),
                rg=request.POST.get("rg"),
                date_of_birth=request.POST.get("date_of_birth"),
                gender=request.POST.get("gender"),

                # Professional Data
                registration_number = str(teachers.count() + 1).zfill(5),
                education_level=request.POST.get("education_level"),
                degree=request.POST.get("degree"),
                subjects=request.POST.get("subjects"),
                is_coordinator = request.POST.get("is_coordinator") == "1",
                coordinator_area=request.POST.get("coordinator-area-field"),

                # Contract Data
                contract_type=request.POST.get("contract_type"),
                hire_date=request.POST.get("hire_date"),
                workload=request.POST.get("workload"),
                salary=request.POST.get("salary"),
                photo=request.POST.get("photo"),
                curriculum=request.POST.get("curriculum"),

                # Contact Data
                email=request.POST.get("email"),
                phone=request.POST.get("phone"),

                # Adress Data
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

            if (transaction == 'create'):
                messages.success(request, "Professor e login criados com sucesso!")
                return redirect("administrator:list_teachers")

        except Exception as e:
            print("ERRO AO CRIAR Professor:", e)
            messages.error(request, f"Erro ao cadastrar professor: {e}")

        context = {
        "is_edit": False,
        "form_action": reverse("teacher:teacher_create_account"),
        "teacher": None,
        'page': 'list_teachers',
        'open_teacher_model': False,
        }
    return render(request, "teachers/list.html", context)



@transaction.atomic
def teacher_edit_account(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == "POST":
        try:
            # Personal Data [User]
            teacher.first_name=request.POST.get("first_name"),
            teacher.last_name=request.POST.get("last_name"),
            teacher.cpf=request.POST.get("cpf"),
            teacher.rg=request.POST.get("rg"),
            teacher.date_of_birth=request.POST.get("date_of_birth"),
            teacher.gender=request.POST.get("gender"),
            # Professional Data
            teacher.registrarion_number= str(teacher.id).zfill(5),
            teacher.education_level=request.POST.get("education_level"),
            teacher.degree=request.POST.get("degree"),
            teacher.subjects=request.POST.get("subjects"),
            teacher.is_coordinator=request.POST.get("is_coordinator"),
            teacher.coordinator_area=request.POST.get("coordinator-area-field"),
            # Contract Data
            teacher.contract_type=request.POST.get("contract_type"),
            teacher.hire_date=request.POST.get("hire_date"),
            teacher.workload=request.POST.get("workload"),
            teacher.salary=request.POST.get("salary"),
            teacher.photo=request.POST.get("photo"),
            teacher.curriculum=request.POST.get("curriculum"),
            # Contact Data
            teacher.email=request.POST.get("email"),
            teacher.phone=request.POST.get("phone"),
            # Adress Data
            teacher.address=request.POST.get("address"),
            teacher.address_number=request.POST.get("address_number"),
            teacher.complement=request.POST.get("complement"),
            teacher.neighborhood=request.POST.get("neighborhood"),
            teacher.zip_code=request.POST.get("zip_code"),
            teacher.city=request.POST.get("city"),
            teacher.state=request.POST.get("state"),

            teacher.save()

            messages.success(request, "Dados do professor atualizados com sucesso!")
            return redirect("administrator:list_teachers")

        except Exception as e:
            print("ERRO AO EDITAR Professor:", e)
            messages.error(request, f"Erro ao atualizar professor: {e}")

    context = {
        'teacher': teacher,
        'page': 'list_teachers',
        'open_teacher_modal': False,

        "is_edit": True,
        "form_action": reverse("teacher:teacher_create_account", args=[teacher.id]),
    }

    return render(request, "dashboard_admin/dashboard.html", context)
