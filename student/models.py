from django.db import models
from accounts.models import PersonUser

class Student(PersonUser):
    """
    Modelo especializado para estudantes, herda de BaseUser
    """
    
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


    # Campos específicos do estudante
    enrollment_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Matrícula'
    )
    
    grade_level = models.CharField(
        max_length=20,
        choices=GRADE_LEVEL_CHOICES,
        verbose_name='Nível de Ensino'
    )
    
    specific_grade = models.CharField(
        max_length=20,
        choices=SPECIFIC_GRADE_CHOICES,
        verbose_name='Série/Ano'
    )
    
    shift = models.CharField(
        max_length=20,
        choices=[
            ('MATUTINO', 'Matutino'),
            ('VESPERTINO', 'Vespertino'),
            ('NOTURNO', 'Noturno'),
            ('INTEGRAL', 'Integral'),
        ],
        verbose_name='Turno'
    )
    
    enrollment_date = models.DateField(
        verbose_name='Data de Matrícula',
        auto_now_add=True
    )
    
    father_name = models.CharField(max_length=100, verbose_name='Nome do Pai', blank=True, null=True)
    mother_name = models.CharField(max_length=100, verbose_name='Nome da Mãe', blank=True, null=True)
    guardian_name = models.CharField(max_length=100, verbose_name='Responsável', blank=True, null=True)
    guardian_phone = models.CharField(max_length=15, verbose_name='Telefone do Responsável', blank=True, null=True)
    
    photo = models.ImageField(
        upload_to='students/photos/',
        verbose_name='Foto',
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = 'Estudante'
        verbose_name_plural = 'Estudantes'
        ordering = ['enrollment_number']
    
    def __str__(self):
        return f'{self.full_name} - {self.enrollment_number}'