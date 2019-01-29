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
from evl import views


def administrador(request):
    if request.user.profile.role == 1:
        return render(request, 'administrador.html')
    else:
        return redirect(views.homeAluno)

def cursosPendentes(request):
    if request.user.profile.role == 1:
        req = requests.get('http://localhost:3000/api/v1/cursos/avaliar')
        print(req.content)
        cursos = json.loads(req.content)
        return render(request, 'cursosPendentes.html', {'cursos': cursos})
    else:
        return redirect(views.homeAluno)

def aprovar_curso(request, curso, categoria):
    if request.user.profile.role == 1:
        req = requests.post('http://localhost:3000/api/v1/cursos/avaliar', data={"id": curso, "category": 1, "status": "Aprovado"})
        return redirect(cursosPendentes)
    else:
        return redirect(views.homeAluno)


def reprovar_curso(request, curso, categoria):
    if request.user.profile.role == 1:
        req = requests.post('http://localhost:3000/api/v1/cursos/avaliar', data={"id": curso, "category": 1, "status": "Reprovado"})
        return redirect(cursosPendentes)
    else:
        return redirect(views.homeAluno)
