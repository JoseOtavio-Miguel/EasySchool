from django.urls import path
from administrator import views as admin_views

app_name = 'administrator'

urlpatterns = [
    # Dashboard #
    path('dashboard/', admin_views.dashboard, name='dashboard'),

    # Student management Urls #
    path('dashboard/list/student', admin_views.list_students, name='list_students'),
    path('desativar/<int:student_id>/', admin_views.deactivate_student, name='deactivate_student'),
    path('load/', admin_views.load_student, name='load_student'), # Rota para salvar (criar/editar)


    # Rota para buscar JSON #
    # urls.py
    path('students/<int:student_id>/json/', admin_views.student_detail, name='student_detail_json'),

    # Teacher management Urls #
    path('dashboard/list/teacher', admin_views.list_teachers, name='list_teachers'),
    path("dashboard/list/teacher/create", admin_views.teacher_create_account, name="teacher_create_account"),
    path("dashboard/list/teacher/edit/<int:teacher_id>/", admin_views.teacher_edit_account,
    name="teacher_edit_account"),
    path('desativar/<int:teacher_id>/', admin_views.deactivate_teacher, name='deactivate_teacher'),


]
