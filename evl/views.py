# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect,get_object_or_404
import xlsxwriter
import requests
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.core.validators import validate_email
from .forms import ContactUsForm
from django.core.mail import EmailMessage
from datetime import datetime
from urllib.request import urlopen
import urllib.parse
import urllib.request
from django.contrib import messages
from django.template import context
from datetime import datetime

def home(request):
    return render(request, 'evl/home.html')

def cursos(request):
    response_cursos = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/cursos')
    response_categorias = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/categorias_cursos')

    cursos = response_cursos.json()
    cursos = json.loads(json.dumps(cursos))
    cursos = cursos['cursos']

    categorias = response_categorias.json()
    categorias = json.loads(json.dumps(categorias))
    categorias = categorias['categorias_cursos']

    return render(request, 'evl/cursos.html', {'cursos' : cursos, 'categorias' : categorias})

def login(request):
    return render(request, 'evl/login.html')

def faleConosco(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print("FOrma = ", form.data)

            print("JSON", json.dumps(form.data))
            req = urllib.request.Request('https://escolamodelows.interlegis.leg.br/api/v1/fale_conosco/adicionar')
            req.add_header('Content-Type', 'application/json; charset=utf-8')
            result = urlopen(req, json.dumps(form.data).encode('utf-8'))
            return render(request, 'evl/home.html', context={'messagem_faleConosco': "A mensagem foi enviada com sucesso"})
        else:
            print("ERROS =", form.errors)
            return render(request, 'evl/faleConosco.html', {'form': form})

    else:
        form = ContactUsForm()
        return render(request, 'evl/faleConosco.html', {'form': form})

def mensagensFaleConosco(request):
    if request.method == "POST":
        id = request.POST['id']
        req = requests.post('https://escolamodelows.interlegis.leg.br/api/v1/fale_conosco/mensagens?conversation_id=' + id)
        # data = json.dumps(req.content.decode(encoding="utf-8"))
        data = req.content.decode(encoding="utf-8")
        return HttpResponse(data, content_type='application/json')
    else:
        req = requests.post('https://escolamodelows.interlegis.leg.br/api/v1/fale_conosco/conversa?school_initials=SSL&page=1&limit=20&not_answered=false')
        messages = json.loads(req.content)
        return render(request, 'evl/mensagensFaleConosco.html', {'messages': messages})

def cadastro(request):
    return render(request, 'evl/cadastro.html')

def meusCursos(request):
    return render(request, 'evl/meusCursos.html')

def certificados(request):
    req = requests.get('https://escolamodelows.interlegis.leg.br/api/v1/certificados?cpf=000.000.000-00')
    certs = json.loads(req.content)
    return render(request, 'evl/certificados.html', {'certs': certs})

def comprovantes(request):
    return render(request, 'evl/comprovantes.html')

def homeAluno(request):
    return render(request, 'evl/homeAluno.html')

def baseCursos(request):
    return render(request, 'evl/baseCursos.html')
