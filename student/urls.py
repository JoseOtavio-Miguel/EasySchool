from django.urls import path
from student import views as student_views

app_name = 'student'

urlpatterns = [
    path('dashboard/', student_views.dashboard, name='dashboard'),
    path('student/create_account', student_views.student_create_account, name="student_create_account"),
    path("student/edit/<int:student_id>/", student_views.student_edit_account, name="student_edit_account"),
]
