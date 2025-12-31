from django.shortcuts import render, redirect, get_object_or_404    
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from django.db import transaction
from django.http import JsonResponse

# Form Import
from administrator.forms import StudentForm 

# Models Import
from accounts.models import User
from student.models import Student
from teacher.models import Teacher
 


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
        "is_edit_teacher": False,
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

        "is_edit_teacher": True,
        "form_action": reverse("teacher:teacher_create_account"),
    }

    return render(request, "dashboard_admin/dashboard.html", context)


# Dashboard view - Redirect to user´s dashboard [ User / Teacher / Admin ...]
@login_required
def dashboard(request):
    if request.user.role != 'student':
        return redirect('administrator:dashboard')
    return render(request, 'dashboard_student/dashboard.html')


# Create your views here.
def index(request):
    return render(request, 'homepage.html')


#### STUDENT´S VIEWS ####

@transaction.atomic
def load_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        
        try:
            # EDIT MODE
            if student_id and student_id.strip():
                student = get_object_or_404(Student, id=student_id)
                mode = "editado"
            # CREATE MODE
            else:
                student = Student()
                mode = "criado"
            
            # Preencher dados
            student.first_name = request.POST.get('first_name')
            student.last_name = request.POST.get('last_name')
            student.cpf = request.POST.get('cpf')
            student.rg = request.POST.get('rg', '')
            student.date_of_birth = request.POST.get('date_of_birth')
            student.gender = request.POST.get('gender')
            
            # Academic
            student.enrollment_number = request.POST.get('enrollment_number')
            student.grade_level = request.POST.get('grade_level')
            student.specific_grade = request.POST.get('specific_grade')
            student.shift = request.POST.get('shift')
            
            # Contact
            student.father_name = request.POST.get('father_name', '')
            student.mother_name = request.POST.get('mother_name', '')
            student.guardian_name = request.POST.get('guardian_name', '')
            student.email = request.POST.get('email')
            student.phone = request.POST.get('phone')
            student.guardian_phone = request.POST.get('guardian_phone', '')
            
            # Address
            student.address = request.POST.get('address')
            student.address_number = request.POST.get('address_number')
            student.complement = request.POST.get('complement', '')
            student.neighborhood = request.POST.get('neighborhood')
            student.zip_code = request.POST.get('zip_code')
            student.city = request.POST.get('city')
            student.state = request.POST.get('state')
            
            # Salvar
            student.save()
            
            messages.success(request, f'Estudante {mode} com sucesso!')
            return redirect('student:dashboard')
            
        except Exception as e:
            messages.error(request, f'Erro ao salvar: {str(e)}')
            return redirect('student:dashboard')
    
    return redirect('student:dashboard')




def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    return JsonResponse({
        "id": student.id,
        "first_name": student.first_name or '',
        "last_name": student.last_name or '',
        "cpf": student.cpf or '',
        "rg": student.rg or '',
        "date_of_birth": student.date_of_birth.isoformat() if student.date_of_birth else '',
        "gender": student.gender or '',
        "enrollment_number": student.enrollment_number or '',
        "grade_level": student.grade_level or '',
        "specific_grade": student.specific_grade or '',
        "shift": student.shift or '',
        "father_name": student.father_name or '',
        "mother_name": student.mother_name or '',
        "guardian_name": student.guardian_name or '',
        "email": student.email or '',
        "phone": student.phone or '',
        "guardian_phone": student.guardian_phone or '',
        "address": student.address or '',
        "address_number": student.address_number or '',
        "complement": student.complement or '',
        "neighborhood": student.neighborhood or '',
        "zip_code": student.zip_code or '',
        "city": student.city or '',
        "state": student.state or ''
    })

