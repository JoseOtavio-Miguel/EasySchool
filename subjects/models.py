from django.db import models
from teacher.models import Teacher

# Create your models here.
class Subjects(models.Model):
    id = models.IntegerField(max_length=50)

    name = models.Charfield(max_leght=50, verbose_name="Nome da Disciplina")

    teacher_id = models.ForeignKey("Teacher", verbose_name=_("Teacher ID"), on_delete=models.CASCADE)
