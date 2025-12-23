from django.urls import path
from administrator import views as admin_views
from student import views as student_views

app_name = 'administrator'

urlpatterns = [
    path('dashboard/', admin_views.dashboard, name='dashboard'),
    path('student/create_student_account', student_views.student_create_account, name='student_create_accout'),
]
