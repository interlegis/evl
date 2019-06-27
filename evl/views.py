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

from django.contrib.auth import logout

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
    return render(request, 'evl/perfilAluno.html')

def userLogout(request):
    logout(request)
    return redirect(settings.BASE_URL + 'log_out?externo=' + 'https://evl.interlegis.leg.br/') #Alterar essa URL para produção
