from django.db import models


# Create your models here.
class ClassRoom(models.Model):

    GRADE_LEVEL_CHOICES = [
        ('INFANTIL', 'Educação Infantil'),
        ('FUNDAMENTAL1', 'Ensino Fundamental I'),
        ('FUNDAMENTAL2', 'Ensino Fundamental II'),
        ('MEDIO', 'Ensino Médio'),
        ('SUPERIOR', 'Ensino Superior'),
    ]
    
    SPECIFIC_GRADE_CHOICES = [
        ('1ANO', '1º Ano'), ('2ANO', '2º Ano'), ('3ANO', '3º Ano'),
        ('4ANO', '4º Ano'), ('5ANO', '5º Ano'), ('6ANO', '6º Ano'),
        ('7ANO', '7º Ano'), ('8ANO', '8º Ano'), ('9ANO', '9º Ano'),
        ('1MEDIO', '1º Ano EM'), ('2MEDIO', '2º Ano EM'), ('3MEDIO', '3º Ano EM'),
    ]


    name = models.CharField(
        max_length=50, 
        verbose_name="Nome do curso")

    grade_level = models.CharField(
        max_length=50, 
        verbose_name="Nível de Ensino", 
        choices=GRADE_LEVEL_CHOICES)

    specific_grade = models.CharField(
        max_length=50)

    year = models.DateField(
        auto_now=False, 
        auto_now_add=False)(
        verbose_name="Ano do curso")

    max_students = models.IntegerField(
        verbose_name="Máximo de Estudantes por Turma")
