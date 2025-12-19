from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

class PersonUser(models.Model):
    """
    Modelo base abstrato para todos os usuários do sistema
    """

    # Informações básicas
    first_name = models.CharField(
        max_length=100,
        verbose_name='Nome',
        validators=[MinLengthValidator(2)]
    )
    
    last_name = models.CharField(
        max_length=100,
        verbose_name='Sobrenome',
        validators=[MinLengthValidator(2)]
    )
    
    cpf = models.CharField(
        max_length=14,
        unique=True,
        verbose_name='CPF',
        help_text='Formato: 000.000.000-00'
    )
    
    rg = models.CharField(
        max_length=20,
        verbose_name='RG',
        blank=True,
        null=True
    )
    
    date_of_birth = models.DateField(
        verbose_name='Data de Nascimento'
    )
    
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
        ('N', 'Prefiro não informar'),
    ]
    
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        verbose_name='Gênero'
    )
    
    # Contato
    email = models.EmailField(
        verbose_name='E-mail',
        unique=True
    )
    
    phone = models.CharField(
        max_length=15,
        verbose_name='Telefone',
        help_text='Formato: (00) 00000-0000'
    )
    
    # Endereço
    address = models.CharField(max_length=200, verbose_name='Endereço')
    address_number = models.CharField(max_length=10, verbose_name='Número')
    complement = models.CharField(max_length=100, verbose_name='Complemento', blank=True, null=True)
    neighborhood = models.CharField(max_length=100, verbose_name='Bairro')
    city = models.CharField(max_length=100, verbose_name='Cidade')
    state = models.CharField(max_length=2, verbose_name='Estado', help_text='Sigla (ex: SP)')
    zip_code = models.CharField(max_length=9, verbose_name='CEP', help_text='00000-000')
    
    # Metadados
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    
    @property
    def full_name(self):
        """Retorna o nome completo"""
        return f'{self.first_name} {self.last_name}'
    
    def age(self):
        """Calcula a idade"""
        from datetime import date
        
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.full_name


