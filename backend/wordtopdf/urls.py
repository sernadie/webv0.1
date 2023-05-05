from django.urls import path
from . import views

urlpatterns = [
    path('wordtopdf/', views.WordToPDFView.as_view(), name='word-to-pdf'),
    path('convert/', views.WordToPDFView.as_view(), name='convert-to-pdf'),
]
