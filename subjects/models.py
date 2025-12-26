from django.db import models
from teacher.models import Teacher


GRADE_CHOICES = (
    'INFANTIL', 'ENSINO INFANTIL',
    'FUNDAMENTAL', 'Ensino Fundamental',
    'MEDIO', 'Ensino Médio',
    'SUPERIOR', 'Ensino Superior',
)
# Create your models here.
class Subjects(models.Model):
    name = models.Charfield(max_leght=50, verbose_name="Nome da Disciplina")
    grade = models.Charfield(max_lenght=50, choices=GRADE_CHOICES, verbose_name="Grau da Disciplina")
    total_hours = models.IntegerField(verbose_name="Montante de Horas")
    week_hours = models.IntegerField(verbose_name="Quantidade de horas por semana")
