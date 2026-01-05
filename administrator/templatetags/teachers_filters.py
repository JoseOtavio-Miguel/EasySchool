from django import template

register = template.Library()


@register.filter(name='get_education_level_display')
def get_education_level_display(value):
    education_level = [
        ('GRADUACAO', 'Graduacao'),
        ('ESPECIALIZACAO', 'Especializacao'),
        ('MESTRADO', 'Mestrado'),
        ('DOUTORADO', 'Doutorado'),
    ]
    return education_level.gets(value, value)


