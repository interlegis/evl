# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import xlsxwriter
import requests
import json
from .models import *
from django.shortcuts import render_to_response
from .forms import FaleConoscoForm, FaleConoscoLoggedForm
from urllib.request import urlopen
import urllib.parse
import urllib.request
from django.template import context
from django.http.response import HttpResponse

#@login_required(login_url='http://localhost:3000/log_in?return=XXX')
def faleConosco(request):
    if request.method == "POST":
        if request.user.is_anonymous:
            formNotLogged = FaleConoscoForm(request.POST)
            if formNotLogged.is_valid():
                req = urllib.request.Request(settings.BASE_URL + 'api/v1/fale_conosco/adicionar')
                req.add_header('Content-Type', 'application/json; charset=utf-8')
                result = urlopen(req, json.dumps(formNotLogged.data).encode('utf-8'))
                return render(request, 'evl/home.html', context={'messagem_faleConosco': "A mensagem foi enviada com sucesso"})
            else:
                print("ERROS =", formNotLogged.errors)
                return render(request, 'faleConosco.html', {'form': formNotLogged})
        else:
            formLogged = FaleConoscoLoggedForm(request.POST)
            if formLogged.is_valid():
                formLogged.fields['name'] = request.user.username
                formLogged.fields['email'] = request.user.email
                formLogged.fields['cpf'] = request.user.username
                formLogged.fields['phone_number'] = request.user.profile.phone
                req = urllib.request.Request(settings.BASE_URL + 'api/v1/fale_conosco/adicionar?name=' + request.user.username + "&email="+ request.user.email + "&cpf=" + request.user.username )
                req.add_header('Content-Type', 'application/json; charset=utf-8')
                result = urlopen(req, json.dumps(formLogged.data).encode('utf-8'))
                return render(request, 'evl/home.html', context={'messagem_faleConosco': "A mensagem foi enviada com sucesso"})
            else:
                print("ERROS =", form.errors)
                return render(request, 'faleConosco.html', {'form': formLogged})

    else:
        form = FaleConoscoForm()
        return render(request, 'faleConosco.html', {'form': form})

def mensagensFaleConosco(request):
    if request.method == "POST":
        id = request.POST['id']
        req = requests.post(settings.BASE_URL + 'api/v1/fale_conosco/mensagens?conversation_id=' + id)
        data = req.content.decode(encoding="utf-8")
        return HttpResponse(data, content_type='application/json')
    else:
        req = requests.post(settings.BASE_URL + 'api/v1/fale_conosco/conversa_usuario?cpf=' + request.user.username)
        messages = json.loads(req.content)
        return render(request, 'mensagensFaleConosco.html', {'messages': messages})
