from django import forms
from .models import ClassRoom

class ClassRoomForms(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = [
            "name", 
            "grade_level", 
            "specific_grade", 
            "year", 
            "max_students"
        ]