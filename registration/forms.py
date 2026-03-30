from django import forms
from .models import Student, Project


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','email']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['topic','languages_used','duration']