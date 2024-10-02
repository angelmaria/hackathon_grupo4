# api/forms.py

from django import forms
from .models import Enrollment, Student, Teacher, Instrument, ClassPack, Price


# Formulario para el modelo Enrollment
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'  # Todos los campos del modelo Enrollment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'   

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'  
        
class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = '__all__'

class ClassPackForm(forms.ModelForm):
    class Meta:
        model = ClassPack
        fields = ['name']

class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = '__all__'