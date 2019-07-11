# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import xlsxwriter
import requests
import json
import urllib.parse
import urllib.request
from django.http.response import HttpResponse
from administrador import views
from .forms import PerfilForm
from django.contrib.auth import logout
from urllib.request import urlopen

def home(request):
    # response_analise = requests.get('http://localhost:3000/analise')
    response_analise = requests.get(settings.BASE_URL + 'analise')
    analises = response_analise.json()
    return render(request, 'evl/home.html', {'analises': analises})

#@login_required()
def login(request):
    return render(request, 'evl/login.html')
    #return HttpResponse('Secret contents!', status=200)

def cadastro(request):
    return render(request, 'evl/cadastro.html')

#@login_required(login_url='http://localhost:3000/log_in?return=URL')
def homeAluno(request):
    if request.user.profile.role == 1:
        return redirect(views.administrador)
    else:
        return render(request, 'evl/homeAluno.html')

def dashboard(request):
    return render(request, 'evl/dashboard.html')

def iFrameDashboard(request):
    return render(request, 'evl/iFrameDashboard.html')


#@login_required(login_url='http://localhost:3000/log_in?return=URL')
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)

def perfilaluno(request):
    form = PerfilForm(
        initial={
            'name': request.user.first_name,
            'email': request.user.email,
            'cpf': request.user.username,
            'phone': request.user.profile.phone,
        }
    )
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            payload = {
                'user': {
                    'birth': str(form.cleaned_data['birth_date'].date()),
                    'email': form.cleaned_data['email'],
                    'cpf': request.user.username,
                    'phone': '33756315',
                }
            }

            req = urllib.request.Request(settings.BASE_URL + 'users/?cpf_antigo=' + request.user.username) 
            req.add_header('Content-Type', 'application/json; charset=utf-8')
            req.get_method = lambda: 'PATCH'
            result = urlopen(req, json.dumps(payload).encode('utf-8'))
            return render(request, 'evl/perfilAluno.html', {'form': form})
        else:
            return render(request, 'evl/perfilAluno.html', {'form': form})
    return render(request, 'evl/perfilAluno.html', {'form': form})

def userLogout(request):
    logout(request)
    # return redirect(settings.BASE_URL + 'log_out?externo=' + 'https://evl.interlegis.leg.br/') #Alterar essa URL para produção
    return redirect(settings.BASE_URL + 'log_out?externo=' + 'http://localhost:8000/') #Alterar essa URL para produção
