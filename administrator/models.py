from django.db import models
from accounts.models import BaseUser

class Administrator(BaseUser):
    """
    Modelo especializado para administradores, herda de BaseUser
    """
    
    DEPARTMENT_CHOICES = [
        ('DIRECAO', 'Direção'),
        ('SECRETARIA', 'Secretaria'),
        ('FINANCEIRO', 'Financeiro'),
        ('RH', 'Recursos Humanos'),
        ('PEDAGOGICO', 'Pedagógico'),
        ('TI', 'Tecnologia da Informação'),
        ('MANUTENCAO', 'Manutenção'),
        ('LIMPEZA', 'Limpeza'),
    ]
    
    # Campos específicos do administrador
    employee_id = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='ID do Funcionário'
    )
    
    department = models.CharField(
        max_length=20,
        choices=DEPARTMENT_CHOICES,
        verbose_name='Departamento'
    )
    
    position = models.CharField(
        max_length=100,
        verbose_name='Cargo'
    )
    
    hire_date = models.DateField(verbose_name='Data de Contratação')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salário')
    
    access_level = models.IntegerField(
        verbose_name='Nível de Acesso',
        choices=[(1, 'Básico'), (2, 'Intermediário'), (3, 'Administrador')],
        default=1
    )
    
    is_supervisor = models.BooleanField(default=False, verbose_name='É Supervisor?')
    
    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
        ordering = ['employee_id']
    
    def has_admin_access(self):
        """Verifica se tem acesso de administrador"""
        return self.access_level >= 3