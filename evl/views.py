# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect,get_object_or_404
import xlsxwriter
import requests
import json
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers

def home(request):
    return render(request, 'evl/home.html')

def cursos(request):
    response_cursos = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/cursos')
    response_categorias = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/categorias_cursos')

    # print(cursos['cursos'][0][0])

    cursos = response_cursos.json()
    cursos = json.loads(json.dumps(cursos))
    cursos = cursos['cursos']
    
    categorias = response_categorias.json()
    categorias = json.loads(json.dumps(categorias))
    categorias = categorias['categorias_cursos']

    return render(request, 'evl/cursos.html', {'cursos' : cursos, 'categorias' : categorias})

def login(request):
    return render(request, 'evl/login.html')

def cadastro(request):
    return render(request, 'evl/cadastro.html')
