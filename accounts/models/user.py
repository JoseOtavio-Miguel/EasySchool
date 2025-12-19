from django.contrib.auth.models import AbstractUser
from django.db import models
from .base import PersonUser



class User(AbstractUser, PersonUser):

    ROLE_CHOICES = (
        ('student', 'Estudante'),
        ('teacher', 'Professor'),
        ('admin', 'Administrador'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
