from django.urls import path
from administrator import views as admin_views

app_name = 'administrator'

urlpatterns = [
    # Dashboard #
    path('dashboard/', admin_views.dashboard, name='dashboard'),

    # Student management Urls #
    path('dashboard/list/student', admin_views.list_students, name='list_students'),
    path('load/student', admin_views.load_student, name='load_student'), # Rota para salvar (criar/editar)
    #path('desativar/<int:student_id>/', admin_views.deactivate_student, name='deactivate_student'),


    # Teacher management Urls #
    path('dashboard/list/teacher', admin_views.list_teachers, name='list_teachers'),
    path('load/teacher', admin_views.load_teacher, name='load_teacher'),
    #path('desativar/<int:teacher_id>/', admin_views.deactivate_teacher, name='deactivate_teacher'),


    # Rota para buscar JSON #
    path('students/<int:student_id>/json/', admin_views.student_detail, name='student_detail_json'),
    path('teachers/<int:teacher_id>/json/', admin_views.teachers_detail, name='teachers_detail_json'),


]
