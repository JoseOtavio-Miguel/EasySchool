from django import template

register = template.Library()


@register.filter(name='get_education_level_display')
def get_education_level_display(value):
    levels = {
        'GRADUAÇÃO': 'Graduação',
        'ESPECIALIZAÇÃO': 'Especialização',
        'MESTRADO': 'Mestrado',
        'DOUTORADO': 'Doutorado',
    }
    return levels.get(value, value)


@register.filter(name='get_contract_type_display')
def get_contract_type_display(value):
    contracts = {
        'CLT': 'CLT',
        'PJ': 'Pessoa Jurídica',
        'TEMPORARIO': 'Temporário',
        'HORISTA': 'Horista',
    }
    return contracts.get(value, value)


@register.filter(name='get_shift_display')
def get_shift_display(value):
    shifts = {
        'MATUTINO': 'Matutino',
        'VESPERTINO': 'Vespertino',
        'NOTURNO': 'Noturno',
        'INTEGRAL': 'Integral',
    }
    return shifts.get(value, value)
