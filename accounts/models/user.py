from django.contrib.auth.models import AbstractUser
from django.db import models
from .base import PersonUser
from student.models import Student



class User(AbstractUser):

    ROLE_CHOICES = (
        ('student', 'Estudante'),
        ('teacher', 'Professor'),
        ('admin', 'Administrador'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    student = models.OneToOneField(
        Student,
        verbose_name=("student"), 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='user'
    )

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
