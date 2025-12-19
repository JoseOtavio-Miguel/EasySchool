from django.urls import path
from administrator import views as admin_views

app_name = 'administrator'

urlpatterns = [
    path('dashboard/', admin_views.dashboard, name='dashboard'),
]
