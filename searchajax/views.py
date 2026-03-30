from django.shortcuts import render
from django.http import JsonResponse
from .models import Student


def home(request):
    return render(request,'searchajax/search.html')


def search(request):

    query = request.GET.get('query')

    students = Student.objects.filter(
        first_name__icontains=query
    )

    data = []

    for s in students:
        data.append({
            'name': s.first_name + " " + s.last_name,
            'courses': [c.name for c in s.courses.all()]
        })

    return JsonResponse({'results': data})