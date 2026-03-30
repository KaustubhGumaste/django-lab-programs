from django.urls import path
from . import views

urlpatterns = [
path('<int:s>/<int:n>/', views.table),
]