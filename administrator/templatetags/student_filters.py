# student/templatetags/student_filters.py
from django import template

register = template.Library()

@register.filter(name='get_grade_level_display')
def get_grade_level_display(value):
    """
    Retorna o display name para o nível de ensino.
    """
    grade_levels = {
        'FUNDAMENTAL1': 'Fundamental I',
        'FUNDAMENTAL2': 'Fundamental II',
        'MEDIO': 'Ensino Médio',
        'SUPERIOR': 'Ensino Superior',
    }
    return grade_levels.get(value, value)

@register.filter(name='get_grade_display')
def get_grade_display(value):
    """
    Retorna o display name para o ano/série.
    Adapte conforme seus modelos.
    """
    grades = {
        '1ANO': '1º Ano',
        '2ANO': '2º Ano',
        '3ANO': '3º Ano',
        '4ANO': '4º Ano',
        '5ANO': '5º Ano',
        '6ANO': '6º Ano',
        '7ANO': '7º Ano',
        '8ANO': '8º Ano',
        '9ANO': '9º Ano',
        '1SERIE': '1ª Série',
        '2SERIE': '2ª Série',
        '3SERIE': '3ª Série',
    }
    return grades.get(value, value)

@register.filter(name='get_shift_display')
def get_shift_display(value):
    """
    Retorna o display name para o turno.
    """
    shifts = {
        'MORNING': 'Manhã',
        'AFTERNOON': 'Tarde',
        'NIGHT': 'Noite',
        'FULL': 'Integral',
    }
    return shifts.get(value, value)