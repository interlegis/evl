from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import xlsxwriter
import requests
import json
from .models import *
from django.shortcuts import render_to_response
from urllib.request import urlopen
import urllib.parse
import urllib.request
from django.template import context
from django.http.response import HttpResponse


def administrador(request):
    return render(request, 'administrador.html')

def cursosPendentes(request):
    req = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/cursos/avaliar')
    print(req.content)
    cursos = json.loads(req.content)
    return render(request, 'cursosPendentes.html', {'cursos': cursos})

def aprovar_curso(request, curso, categoria):
    req = requests.post('https://escolamodelows.interlegis.leg.br/api/v1/cursos/avaliar', data={"id": curso, "category": 1, "status": "Aprovado"})
    return redirect(cursosPendentes)


def reprovar_curso(request, curso, categoria):
    req = requests.post('https://escolamodelows.interlegis.leg.br/api/v1/cursos/avaliar', data={"id": curso, "category": 1, "status": "Reprovado"})
    return redirect(cursosPendentes)
