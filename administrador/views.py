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
        req1 = requests.get('http://localhost:3000/api/v1/categorias_cursos?key=' + request.user.profile.key)
        categorias = json.loads(req1.content)
        print(categorias)
        req2 = requests.get('http://localhost:3000/api/v1/cursos/aprovar?key=' + request.user.profile.key)
        cursos = json.loads(req2.content)
        return render(request, 'cursosPendentes.html', {'cursos': cursos, 'categorias': categorias})
    else:
        return redirect(views.homeAluno)

def categoriasGestao(request):
    if request.user.profile.role == 1:
        req1 = requests.get('http://localhost:3000/api/v1/categorias_cursos?key=' + request.user.profile.key)
        categorias = json.loads(req1.content)
        return render(request, 'categoriasGestao.html', {'categorias': categorias})
    else:
        return redirect(views.homeAluno)

def criar_categoria(request, nome):
    if request.user.profile.role == 1:
        req = requests.post('http://localhost:3000/api/v1/categorias_cursos/adicionar?key=' + request.user.profile.key, data={'name': nome})
        return redirect(categoriasGestao)
    else:
        return redirect(views.homeAluno)

def editar_categoria(request, categoria, nome):
    if request.user.profile.role == 1:
        req = requests.post('http://localhost:3000/api/v1/categorias_cursos/atualizar?key=' + request.user.profile.key, data={"id": categoria, "name": nome})
        return redirect(categoriasGestao)
    else:
        return redirect(views.homeAluno)

def aprovar_curso(request, curso, categoria):
    if request.user.profile.role == 1:
        req = requests.post('http://localhost:3000/api/v1/cursos/aprovar?key=' + request.user.profile.key, data={"id": curso, "category": categoria, "status": "Aprovado"})
        return redirect(cursosPendentes)
    else:
        return redirect(views.homeAluno)


def reprovar_curso(request, curso, categoria):
    if request.user.profile.role == 1:
        req = requests.post('http://localhost:3000/api/v1/cursos/aprovar?key=' + request.user.profile.key, data={"id": curso, "category": categoria, "status": "Reprovado"})
        return redirect(cursosPendentes)
    else:
        return redirect(views.homeAluno)
