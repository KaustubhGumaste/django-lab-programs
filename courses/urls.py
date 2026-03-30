from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('student/', views.add_student),
    path('course/', views.add_course),
    path('enroll/', views.enroll),
    path('show/', views.show),
]