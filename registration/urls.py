from django.urls import path
from . import views

urlpatterns = [
path('register/', views.register_student),
path('', views.StudentList.as_view()),
path('<int:pk>/', views.StudentDetail.as_view()),
path('csv/', views.download_csv),
]