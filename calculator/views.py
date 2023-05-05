from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework import generics
from .serializers import CalculationSerializer
from django.shortcuts import render, redirect
from decimal import Decimal

def calculadora_calificaciones(request):
    if request.method == 'POST':
        nota = Decimal(request.POST.get('nota'))
        porcentaje = Decimal(request.POST.get('porcentaje'))

        # Guardar la calificación en la sesión
        if 'calificaciones' not in request.session:
            request.session['calificaciones'] = []
        request.session['calificaciones'].append({
            'nota': float(nota),  # Convertir Decimal a float
            'porcentaje': float(porcentaje),  # Convertir Decimal a float
        })
        request.session.modified = True  # Asegurarse de que la sesión se actualice

        calificaciones = request.session['calificaciones']
        suma_porcentajes = sum([calificacion['porcentaje'] for calificacion in calificaciones])

        if suma_porcentajes > 100:
            # Eliminar la última calificación si la suma de los porcentajes es mayor a 100
            calificaciones.pop()
            request.session.modified = True
            return render(request, 'error.html', {'error': 'La suma de los porcentajes no puede ser mayor a 100.'})
        elif suma_porcentajes == 100:
            total = sum([calificacion['nota'] * calificacion['porcentaje'] / 100 for calificacion in calificaciones])
            request.session['calificaciones'] = []  # Limpiar todas las calificaciones al finalizar
            request.session.modified = True
            return render(request, 'resultado.html', {'total': total})

    return render(request, 'calculate.html')
