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

from django.http import HttpResponse
from django.views.generic import View

from django.template.loader import render_to_string
from weasyprint import HTML
from django.core.files.storage import FileSystemStorage

def pdf(request, codigoCertificado):
    req = requests.get(settings.BASE_URL + '/api/v1/certificados/detalhar?code_id=' + codigoCertificado + "&key=" + request.user.profile.key)
    certificado = json.loads(req.content)  
    html_string = render_to_string('pdf/invoice.html', {'certificado': certificado['certificado'], 'codigo': codigoCertificado})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf_file = html.write_pdf();
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=relatorio.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    response.write(pdf_file)
    return response 
    # return render(request, 'pdf/invoice.html')

def certificados(request):
    req = requests.get(settings.BASE_URL + '/api/v1/certificados?cpf=' + request.user.profile.user.username + '&key=' + request.user.profile.key)
    certs = json.loads(req.content)
    return render(request, 'certificados.html', {'certs': certs})

def validarCertificado(request):
    if request.method == "POST":
        form = ValidarCertificadoForm(request.POST)
        if form.is_valid():
            req = requests.get(settings.BASE_URL + '/api/v1/certificados/detalhar?code_id=' + request.POST['code_id'] + "&key=" + request.user.profile.key)
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
        req = requests.get(settings.BASE_URL + '/api/v1/certificados/detalhar?code_id=' + code + "&key=" + request.user.profile.key)
        certificado = json.loads(req.content)
        return render(request, 'certificado.html', {'certificado': certificado['certificado']})
