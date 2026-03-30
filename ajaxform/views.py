from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .forms import StudentForm


def student(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({'status':'success'})

    else:
        form = StudentForm()

    return render(request,'ajaxform/form.html',{'form':form})