from django.db import models


class Institution(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Nome da Instituição'
    )

    short_name = models.CharField(
        max_length=100,
        verbose_name='Nome Curto',
        blank=True
    )

    cnpj = models.CharField(
        max_length=18,
        unique=True,
        verbose_name='CNPJ'
    )

    email = models.EmailField(
        verbose_name='Email Institucional',
        unique=True
    )

    phone = models.CharField(
        max_length=20,
        verbose_name='Telefone',
        help_text='Formato: (00) 00000-0000'
    )

    address = models.CharField(
        max_length=255,
        verbose_name='Endereço'
    )

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=2,
        verbose_name='UF'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Ativa'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )

    class Meta:
        verbose_name = 'Instituição'
        verbose_name_plural = 'Instituições'

    def __str__(self):
        return self.short_name or self.name
