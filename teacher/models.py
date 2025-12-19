from django.db import models
from accounts.models import PersonUser

class Teacher(PersonUser):
    """
    Modelo especializado para professores, herda de BaseUser
    """
    
    EDUCATION_LEVEL_CHOICES = [
        ('GRADUACAO', 'Graduação'),
        ('ESPECIALIZACAO', 'Especialização'),
        ('MESTRADO', 'Mestrado'),
        ('DOUTORADO', 'Doutorado'),
    ]
    
    CONTRACT_TYPE_CHOICES = [
        ('CLT', 'CLT'),
        ('PJ', 'Pessoa Jurídica'),
        ('TEMPORARIO', 'Temporário'),
        ('HORISTA', 'Horista'),
    ]
    
    # Campos específicos do professor
    registration_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Registro Funcional'
    )
    
    education_level = models.CharField(
        max_length=20,
        choices=EDUCATION_LEVEL_CHOICES,
        verbose_name='Nível de Formação'
    )
    
    degree = models.CharField(
        max_length=100,
        verbose_name='Formação',
        help_text='Ex: Licenciatura em Matemática'
    )
    
    subjects = models.CharField(
        max_length=500,
        verbose_name='Disciplinas',
        help_text='Separe com vírgula'
    )
    
    contract_type = models.CharField(
        max_length=20,
        choices=CONTRACT_TYPE_CHOICES,
        verbose_name='Tipo de Contrato'
    )
    
    hire_date = models.DateField(verbose_name='Data de Contratação')
    workload = models.IntegerField(verbose_name='Carga Horária Semanal', default=40)
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salário', blank=True, null=True)
    
    is_coordinator = models.BooleanField(default=False, verbose_name='É Coordenador?')
    coordinator_area = models.CharField(max_length=100, verbose_name='Área de Coordenação', blank=True, null=True)
    
    photo = models.ImageField(
        upload_to='teachers/photos/',
        verbose_name='Foto',
        blank=True,
        null=True
    )
    
    curriculum = models.FileField(
        upload_to='teachers/curriculums/',
        verbose_name='Currículo',
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ['registration_number']
    
    def get_subjects_list(self):
        """Retorna lista de disciplinas"""
        return [s.strip() for s in self.subjects.split(',')] if self.subjects else []