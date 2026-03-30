from django.urls import path
from .views import vc

urlpatterns = [
path('<str:sentence>/', vc),
]