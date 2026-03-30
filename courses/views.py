from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm


def home(request):
    return render(request,'courses/home.html')


def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/courses/')

    return render(request,'courses/student.html',{'form':form})


def add_course(request):
    form = CourseForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/courses/')

    return render(request,'courses/course.html',{'form':form})


def enroll(request):

    students = Student.objects.all()
    courses = Course.objects.all()

    if request.method == "POST":

        s = request.POST['student']
        c = request.POST['course']

        student = Student.objects.get(id=s)
        course = Course.objects.get(id=c)

        course.students.add(student)

    return render(request,'courses/enroll.html',{
        'students':students,
        'courses':courses
    })


def show(request):
    courses = Course.objects.all()
    return render(request,'courses/show.html',{'courses':courses})