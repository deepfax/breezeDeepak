
from django.contrib import admin
from django.urls import path
from .views import rev_str

urlpatterns = [
    path('admin/', admin.site.urls),
    path('revstr/',rev_str),
]
