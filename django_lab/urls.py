from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('prime/', include('prime.urls')),
    path('registration/', include('registration.urls')),
    path('ajax/', include('ajaxform.urls')),
    path('search/', include('searchajax.urls')),

    path('squares/', include('squares.urls')),
    path('vowels/', include('vowels.urls')),
]