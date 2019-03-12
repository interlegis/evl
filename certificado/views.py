# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
import xlsxwriter
import requests
import json
from .forms import ValidarCertificadoForm
from .models import *
import urllib.parse
import urllib.request

def certificados(request):
    req = requests.get(settings.BASE_URL + 'api/v1/certificados?cpf=' + request.user.profile.cpf)
    certs = json.loads(req.content)
    return render(request, 'certificados.html', {'certs': certs})

def validarCertificado(request):
    if request.method == "POST":
        form = ValidarCertificadoForm(request.POST)
        if form.is_valid():
            req = requests.get(settings.BASE_URL + 'api/v1/certificados/detalhar?code_id=' + request.POST['code_id'])
            certificado = json.loads(req.content)
            try:
                print(certificado["message"])
                return render(request, 'validarCertificado.html', {'form': form ,'alerta': certificado["message"]})
            except Exception as e:
                return render(request, 'certificado.html', {'certificado': certificado['certificado']})
        else:
            return render(request, 'validarCertificado.html', {'form': form})
    else:
        form = ValidarCertificadoForm()
        return render(request, 'validarCertificado.html', {'form': form})

def validacaoQrCode(request, code):
    if code:
        req = requests.get(settings.BASE_URL + 'api/v1/certificados/detalhar?code_id=' + code)
        certificado = json.loads(req.content)
        return render(request, 'certificado.html', {'certificado': certificado['certificado']})
