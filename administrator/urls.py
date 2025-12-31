from django.urls import path
from administrator import views as admin_views

app_name = 'administrator'

urlpatterns = [
    path('dashboard/', admin_views.dashboard, name='dashboard'),
    path('dashboard/list/student', admin_views.list_students, name='list_students'),
    path('dashboard/list/student', admin_views.closeModal, name="closeModal"),
    path('dashboard/list/teacher', admin_views.list_teachers, name='list_teachers'),
    
    path("dashboard/list/teacher/create", admin_views.teacher_create_account, name="teacher_create_account"),
    path("dashboard/list/teacher/edit/<int:teacher_id>/", admin_views.teacher_edit_account,
    name="teacher_edit_account"),

    path('dashboard/list/student/edit/num/<int:student_id>', admin_views.openModal_edit, name='openModal_edit'),

    path('editar/<int:student_id>/', admin_views.edit_student, name='edit_student'),
    path('desativar/<int:student_id>/', admin_views.deactivate_student, name='deactivate_student'),

    path('desativar/<int:teacher_id>/', admin_views.deactivate_teacher, name='deactivate_teacher'),
]
