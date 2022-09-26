# pylint: disable=missing-module-docstring
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('minha_consulta', minha_consulta, name='minha_consulta')
]
