from django.urls import path
from administrator import views as admin_views

app_name = 'administrator'

urlpatterns = [
    path('dashboard/', admin_views.dashboard, name='dashboard'),
    path('dashboard/list/student', admin_views.list_students, name='list_students'),
    path('dashboard/list/student', admin_views.closeModal, name="closeModal"),
    path('editar/<int:student_id>/', admin_views.edit_student, name='edit_student'),
    path('dashboard/list/student/edit/num/<int:student_id>', admin_views.openModal, name='openModal'),
    path('desativar/<int:student_id>/', admin_views.deactivate_student, name='deactivate_student'),
]
