# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import xlsxwriter
import requests
import json
from .models import *
import urllib.parse
import urllib.request
from django.conf import settings


def cursos(request):
    response_cursos = requests.get(settings.BASE_URL + 'api/v1/cursos?key=' + settings.APIKEY)
    response_categorias = requests.get(settings.BASE_URL + 'api/v1/categorias_cursos?key=' + settings.APIKEY)

    cursos = response_cursos.json()
    cursos = json.loads(json.dumps(cursos))
    cursos = cursos['cursos']

    categorias = response_categorias.json()
    categorias = json.loads(json.dumps(categorias))
    categorias = categorias['categorias_cursos']

    return render(request, 'cursos.html', {'cursos' : cursos, 'categorias' : categorias})

def meusCursos(request):
    user_cursos = requests.get(settings.BASE_URL + 'api/v1/cursos?key=' + request.user.profile.key)
    cursos = json.loads(user_cursos.content)
    return render(request, 'meusCursos.html', {'cursos': cursos})


def baseCursos(request):
    return render(request, 'baseCursos.html')
