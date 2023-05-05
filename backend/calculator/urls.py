from django.urls import path
from . import views

urlpatterns = [
    path('calculate/', views.calculadora_calificaciones, name='calculate'),
]