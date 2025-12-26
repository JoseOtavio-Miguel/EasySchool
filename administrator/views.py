from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from student.models import Student
from administrator.forms import StudentForm  

# Create your views here.
@login_required
def dashboard(request):
    if request.user.role != 'admin':
        return redirect('login')
    return render(request, 'dashboard_admin/dashboard.html')


def list_students(request):
    # Store all student in students
    students = Student.objects.all()
    print("Quantidade de ", students)

    context = {
        'students': students,
        'page': 'list_students',
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