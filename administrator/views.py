from django.shortcuts import render, redirect, get_object_or_404    
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q

from student.models import Student
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
