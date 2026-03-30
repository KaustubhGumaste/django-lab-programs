from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Student
from .forms import StudentForm, ProjectForm


def register_student(request):

    if request.method == "POST":

        student_form = StudentForm(request.POST)
        project_form = ProjectForm(request.POST)

        if student_form.is_valid() and project_form.is_valid():

            project = project_form.save()

            student = student_form.save(commit=False)
            student.project = project
            student.save()

            return redirect('/registration/')

    else:
        student_form = StudentForm()
        project_form = ProjectForm()

    return render(request,'registration/register.html',{
        'student_form':student_form,
        'project_form':project_form
    })


class StudentList(ListView):
    model = Student
    template_name = "registration/list.html"


class StudentDetail(DetailView):
    model = Student
    template_name = "registration/detail.html"

import csv
from django.http import HttpResponse


def download_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)

    writer.writerow([
        'First Name',
        'Last Name',
        'Email',
        'Project',
        'Languages',
        'Duration'
    ])

    from .models import Student

    for s in Student.objects.all():
        writer.writerow([
            s.first_name,
            s.last_name,
            s.email,
            s.project.topic,
            s.project.languages_used,
            s.project.duration
        ])

    return response