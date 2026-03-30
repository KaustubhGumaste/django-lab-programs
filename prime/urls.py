from django.urls import path
from .views import prime_form, prime_result

urlpatterns = [
    path('', prime_form),
    path('result/', prime_result),
]