# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import xlsxwriter
import requests
import json
from .models import *
import urllib.parse
import urllib.request


def cursos(request):
    response_cursos = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/cursos?key=k4B5YcbKa619ohu3wxk2xXbmtoxFuQqrwcKEOTAnZi7iy4tl9z')
    # response_cursos = requests.get('http://localhost:3000/api/v1/cursos')
    response_categorias = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/categorias_cursos?key=k4B5YcbKa619ohu3wxk2xXbmtoxFuQqrwcKEOTAnZi7iy4tl9z')
    # response_categorias = requests.get('http://localhost:3000/api/v1/categorias_cursos')

    cursos = response_cursos.json()
    cursos = json.loads(json.dumps(cursos))
    cursos = cursos['cursos']

    categorias = response_categorias.json()
    categorias = json.loads(json.dumps(categorias))
    categorias = categorias['categorias_cursos']

    return render(request, 'cursos.html', {'cursos' : cursos, 'categorias' : categorias})

def meusCursos(request):
    user_cursos = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/cursos?key=k4B5YcbKa619ohu3wxk2xXbmtoxFuQqrwcKEOTAnZi7iy4tl9z')
    cursos = json.loads(user_cursos.content)
    return render(request, 'meusCursos.html', {'cursos': cursos})


def baseCursos(request):
    return render(request, 'baseCursos.html')
