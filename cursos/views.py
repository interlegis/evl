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
    response_cursos = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/cursos?key=' + request.user.profile.key)
    response_categorias = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/categorias_cursos?key=' + request.user.profile.key)

    cursos = response_cursos.json()
    cursos = json.loads(json.dumps(cursos))
    cursos = cursos['cursos']

    categorias = response_categorias.json()
    categorias = json.loads(json.dumps(categorias))
    categorias = categorias['categorias_cursos']

    return render(request, 'cursos.html', {'cursos' : cursos, 'categorias' : categorias})

def meusCursos(request):
    user_cursos = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/registros?key=' + request.user.profile.key + '&cpf=' + request.user.profile.cpf)
    cursos = json.loads(user_cursos.content)
    return render(request, 'meusCursos.html', {'cursos': cursos})


def baseCursos(request):
    return render(request, 'baseCursos.html')
