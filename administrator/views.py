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
 

# Views 
# Index View - Redirect to Homepage 
def index(request):
    return render(request, 'homepage.html')


# Dashboard -> Main page for user, include sidebar, footer and the flexible and apropriate content depending on the current page
@login_required
def dashboard(request):
    if request.user.role != 'admin':
        return redirect('login')
    return render(request, 'dashboard_admin/dashboard.html')




# TEACHER´S VIEWS 
# List Teachers -> List all teachers in the form content
def list_teachers(request):
    teachers = Teacher.objects.all()

    q = request.GET.get('q')
    education_level_filter = request.GET.get('education_level')

    if q:
        teachers = teachers.filter(
        Q(first_name__icontains=q) |
        Q(last_name__icontains=q) |
        Q(registration_number__icontains=q) |
        Q(contract_type__icontains=q) 
        )
    
    if education_level_filter:
        teachers = teachers.filter(education_level = education_level_filter)

    context = {
        'teachers': teachers,
        'page': 'list_teachers',
        'open_teacher_modal': request.session.pop('open_teacher_modal', False),
    }

    return render(request, 'dashboard_admin/dashboard.html', context)


# Create and Update Teacher´s Data 
@transaction.atomic
def load_teacher(request):
    if request.method == "POST":
        teacher_id = request.POST.get('teacher_id')

        try:
            if teacher_id and teacher_id.strip():
                teacher = get_object_or_404(Teacher, id=teacher_id)
                mode = "editado"
            else:
                teacher = Teacher()
                mode = "criado"

            # Personal Data
            teacher.first_name = request.POST.get("first_name")
            teacher.last_name = request.POST.get("last_name")
            teacher.cpf = request.POST.get("cpf")
            teacher.rg = request.POST.get("rg", "")
            
            # Handle date fields properly (pode ser vazio)
            date_of_birth = request.POST.get("date_of_birth")
            teacher.date_of_birth = date_of_birth if date_of_birth else None
            
            teacher.gender = request.POST.get("gender")
            
            # Professional Data
            teacher.education_level = request.POST.get("education_level")
            teacher.degree = request.POST.get("degree")
            teacher.subjects = request.POST.get("subjects")
            teacher.is_coordinator = request.POST.get("is_coordinator") == "1"
            teacher.coordinator_area = request.POST.get("coordinator_area", "")
            
            # Contract Data
            teacher.contract_type = request.POST.get("contract_type")
            
            hire_date = request.POST.get("hire_date")
            teacher.hire_date = hire_date if hire_date else None
            
            workload = request.POST.get("workload")
            teacher.workload = int(workload) if workload else None
            
            salary = request.POST.get("salary")
            teacher.salary = float(salary) if salary else None
            
            # Files
            if request.FILES.get("photo"):
                teacher.photo = request.FILES.get("photo")
            if request.FILES.get("curriculum"):
                teacher.curriculum = request.FILES.get("curriculum")
            
            # Contact Data
            teacher.email = request.POST.get("email")
            teacher.phone = request.POST.get("phone")
            
            # Address Data
            teacher.address = request.POST.get("address")
            teacher.address_number = request.POST.get("address_number")
            teacher.complement = request.POST.get("complement", "")
            teacher.neighborhood = request.POST.get("neighborhood")
            teacher.zip_code = request.POST.get("zip_code")
            teacher.city = request.POST.get("city")
            teacher.state = request.POST.get("state")

            # Save teacher
            teacher.save()
            
            # Update registration number after saving (para ter o ID)
            if mode == "criado":
                teacher.registration_number = str(teacher.id).zfill(5)
                teacher.save()

            messages.success(request, f'Professor {mode} com sucesso!')
            return redirect('administrator:list_teachers')

        except Exception as e:
            import traceback
            print(f"Erro completo: {traceback.format_exc()}")  # Para debug
            messages.error(request, f'Erro ao salvar: {str(e)}')
            return redirect('administrator:list_teachers')

    return redirect('administrator:list_teachers')


def teachers_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    return JsonResponse({
        "id": teacher.id,

        # Personal Data
        "first_name": teacher.first_name or '',
        "last_name": teacher.last_name or '',
        "cpf": teacher.cpf or '',
        "rg": teacher.rg or '',
        "date_of_birth": teacher.date_of_birth.isoformat() if teacher.date_of_birth else '',
        "gender": teacher.gender or '',

        # Professional Data
        "registration_number": teacher.registration_number or '',
        "education_level": teacher.education_level or '',
        "degree": teacher.degree or '',
        "subjects": teacher.subjects or '',
        "is_coordinator": teacher.is_coordinator if teacher.is_coordinator is not None else False,
        "coordinator_area": teacher.coordinator_area or '',

        # Contract Data
        "contract_type": teacher.contract_type or '',
        "hire_date": teacher.hire_date.isoformat() if teacher.hire_date else '',
        "workload": teacher.workload or '',
        "salary": str(teacher.salary) if teacher.salary is not None else '',

        # Files / Media
        "photo": teacher.photo.url if teacher.photo else '',
        "curriculum": teacher.curriculum.url if teacher.curriculum else '',

        # Contact Data
        "email": teacher.email or '',
        "phone": teacher.phone or '',

        # Address Data
        "address": teacher.address or '',
        "address_number": teacher.address_number or '',
        "complement": teacher.complement or '',
        "neighborhood": teacher.neighborhood or '',
        "zip_code": teacher.zip_code or '',
        "city": teacher.city or '',
        "state": teacher.state or '',
    })


'''
# Deactive Teacher -> Changes the active status to false but still keeps the user's data in the database
def deactivate_teacher(request, student_id):
    if request.method == 'POST':
        teacher = get_object_or_404(Student, id=student_id)
        teacher.is_active = False
        teacher.save()
        messages.success(request, f'Professor {teacher.name} desativado com sucesso!')
    
    return redirect('administrator:list_teacher')  
'''


# STUDENT´S VIEWS 
# List Students -> List all students in the form content
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



@transaction.atomic
def load_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        
        try:
            # Edit Student
            if student_id and student_id.strip():
                student = get_object_or_404(Student, id=student_id)
                mode = "editado"

            # Create Student
            else:
                student = Student()
                mode = "criado"
            
            # Fill data
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
            return redirect('administrator:list_students')
            
        except Exception as e:
            messages.error(request, f'Erro ao salvar: {str(e)}')
            return redirect('administrator:list_students')
    
    return redirect('administrator:list_students')



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


'''
# Deactive Student -> Changes the active status to false but still keeps the user's data in the database
def deactivate_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        student.is_active = False
        student.save()
        messages.success(request, f'Aluno {student.name} desativado com sucesso!')
    
    return redirect('administrator:list_students')  
'''

