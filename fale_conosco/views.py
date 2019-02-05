# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import xlsxwriter
import requests
import json
from .models import *
from django.shortcuts import render_to_response
from .forms import FaleConoscoForm
from urllib.request import urlopen
import urllib.parse
import urllib.request
from django.template import context
from django.http.response import HttpResponse

#@login_required(login_url='http://localhost:3000/log_in?return=XXX')
def faleConosco(request):
    if request.method == "POST":
        form = FaleConoscoForm(request.POST)
        if form.is_valid():
            # req = urllib.request.Request('http://localhost:3000/api/v1/fale_conosco/adicionar')
            req = urllib.request.Request('http://localhost:3000/api/v1/fale_conosco/adicionar')
            req.add_header('Content-Type', 'application/json; charset=utf-8')
            result = urlopen(req, json.dumps(form.data).encode('utf-8'))
            return render(request, 'evl/home.html', context={'messagem_faleConosco': "A mensagem foi enviada com sucesso"})
        else:
            print("ERROS =", form.errors)
            return render(request, 'faleConosco.html', {'form': form})
    else:
        form = FaleConoscoForm()
        return render(request, 'faleConosco.html', {'form': form})

def mensagensFaleConosco(request):
    if request.method == "POST":
        id = request.POST['id']
        # req = requests.post('http://localhost:3000/api/v1/fale_conosco/mensagens?conversation_id=' + id)
        req = requests.post('http://localhost:3000/api/v1/fale_conosco/mensagens?conversation_id=' + id)
        # data = json.dumps(req.content.decode(encoding="utf-8"))
        data = req.content.decode(encoding="utf-8")
        return HttpResponse(data, content_type='application/json')
    else:
        # req = requests.post('http://localhost:3000/api/v1/fale_conosco/conversa_usuario?cpf=045.232.691-57')
        req = requests.post('http://localhost:3000/api/v1/fale_conosco/conversa_usuario?cpf=045.232.691-57')
        messages = json.loads(req.content)
        return render(request, 'mensagensFaleConosco.html', {'messages': messages})
