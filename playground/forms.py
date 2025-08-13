from django import forms
from .model import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ["name","email","phone","password"]

