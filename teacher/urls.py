from django.urls import path
from teacher import views as teacher_views

app_name = "teacher"    

urlpatterns = [
    path('dashboard/', teacher_views.dashboard, name='dashboard'),
    path('teacher_create_account', teacher_views.teacher_create_account, name="teacher_create_account"),
]
