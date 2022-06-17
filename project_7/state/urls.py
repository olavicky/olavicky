from django.urls import path
from .views import city

urlpatterns = [
    path("", city),


]
