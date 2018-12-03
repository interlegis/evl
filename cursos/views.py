# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import xlsxwriter
import requests
import json
from .models import *
import urllib.parse
import urllib.request
from .forms import AvaliarCursosForm


def cursos(request):
    response_cursos = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/cursos')
    # response_cursos = requests.get('http://localhost:3000/api/v1/cursos')
    response_categorias = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/categorias_cursos')
    # response_categorias = requests.get('http://localhost:3000/api/v1/categorias_cursos')

    cursos = response_cursos.json()
    cursos = json.loads(json.dumps(cursos))
    cursos = cursos['cursos']

    categorias = response_categorias.json()
    categorias = json.loads(json.dumps(categorias))
    categorias = categorias['categorias_cursos']

    return render(request, 'cursos.html', {'cursos' : cursos, 'categorias' : categorias})

def meusCursos(request):
    return render(request, 'meusCursos.html')

def baseCursos(request):
    return render(request, 'baseCursos.html')

def cursosPendentes(request):
    req = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/cursos/avaliar')
    cursos = json.loads(req.content)
    try:
        cursos = cursos['cursos']
        return render(request, 'cursosPendentes.html', {'cursos': cursos})
    except Exception as e:
        return render(request, 'cursosPendentes.html')

def avaliarCursos(request, id):
    if request.method == "POST":
        form = AvaliarCursosForm(request.POST)
        if form.is_valid():
            categoria = request.POST['course_category_id']
            estado = request.POST['status']
            req = requests.post('https://escolamodelows.interlegis.leg.br/api/v1/cursos/avaliar?id='+ id + '&category=' + categoria + '&status=' + estado + '')
            validar = json.loads(req.content)
            print(validar["message"])
            return render(request, 'avaliarCursos.html', {'form': form, 'mensagem_avaliar': validar["message"]})
        else:
            print("ERROS =", form.errors)
            return render(request, 'avaliarCursos.html', {'form': form})
    else:
        form = AvaliarCursosForm()
        return render(request, 'avaliarCursos.html', {'form': form})
