from django.contrib import admin
from django.urls import include, path
import calculator.views
import wordtopdf.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate/', calculator.views.calculadora_calificaciones, name='calculate'),
    path('api/', include('calculator.urls')),
    path('api/wordtopdf/', wordtopdf.views.WordToPDFView.as_view(), name='word-to-pdf'),
    path('api/wordtopdf/convert/', wordtopdf.views.WordToPDFView.as_view(), name='convert-to-pdf'),
]
