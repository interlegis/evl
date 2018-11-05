# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
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
from django.contrib import messages
from django.template import context
from datetime import datetime
from django.http.response import HttpResponse


def home(request):
    return render(request, 'evl/home.html')

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

    return render(request, 'evl/cursos.html', {'cursos' : cursos, 'categorias' : categorias})

#@login_required()
def login(request):
    return render(request, 'evl/login.html')
    #return HttpResponse('Secret contents!', status=200)

#@login_required(login_url='https://escolamodelows.interlegis.leg.br/log_in?return=XXX')
def faleConosco(request):
    
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
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
        req = requests.post('https://escolamodelows.interlegis.leg.br/api/v1/fale_conosco/conversa_usuario?cpf=045.232.691-57')
        messages = json.loads(req.content)
        return render(request, 'evl/mensagensFaleConosco.html', {'messages': messages})
    # else
    #     data = {}
    #     data[""]
    #     req = urllib.request.Request('https://escolamodelows.interlegis.leg.br/api/v1/fale_conosco/adicionar')
    #     req.add_header('Content-Type', 'application/json; charset=utf-8')
    #     result = urlopen(req, json.dumps(form.data).encode('utf-8'))

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

#@login_required(login_url='https://escolamodelows.interlegis.leg.br/log_in?return=URL')
def homeAluno(request):
    return render(request, 'evl/homeAluno.html')

def baseCursos(request):
    return render(request, 'evl/baseCursos.html')

def dashboard(request):
    return render(request, 'evl/dashboard.html')

#@login_required(login_url='https://escolamodelows.interlegis.leg.br/log_in?return=URL')
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)

