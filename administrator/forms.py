# administrator/forms.py
from django import forms
from student.models import Student  # Importe o modelo Student do app student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 
            'email', 
            'enrollment_number', 
            'grade_level', 
            'specific_grade', 
            'shift', 
            'is_active'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@exemplo.com'
            }),
            'enrollment_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de matrícula'
            }),
            'grade': forms.Select(attrs={'class': 'form-control'}),
            'grade_level': forms.Select(attrs={'class': 'form-control'}),
            'shift': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'first_name': 'Nome',
            'email': 'E-mail',
            'enrollment_level': 'Matrícula',
            'grade_level': 'Nível de Ensino',
            'specifc_grade': 'Ano/Série',
            'shift': 'Turno',
            'is_active': 'Ativo',
        }