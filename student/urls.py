from django.urls import path
from student import views as student_views

app_name = 'student'

urlpatterns = [
    path('dashboard/', student_views.dashboard, name='dashboard'),
    
    # Rota para buscar JSON do estudante
    path('students/<int:student_id>/json/', student_views.student_detail, name='student_detail_json'),
    # Rota para salvar (criar/editar)
    path('load/', student_views.load_student, name='load_student'),
    # student/urls.py

    # Rota para buscar JSON
    path('students/<int:student_id>/json/', student_views.student_detail, name='student_detail_json'),

]
