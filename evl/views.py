# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect,get_object_or_404
import xlsxwriter
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.core.validators import validate_email
from .forms import ContactUsForm
from django.core.mail import EmailMessage
from datetime import datetime


def home(request):
    return render(request, 'evl/home.html')

def cursos(request):
    cursos = Courses.objects.all()
    cursos_json = serializers.serialize("json", cursos)
    categorias = CourseCategories.objects.all()
    return render(request, 'evl/cursos.html', {'cursos' : cursos, 'categorias' : categorias, 'cursos_json' : cursos_json})

def fale_conosco(request):
    if request.method == "POST":

        name = request.POST.get('name')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        contato = request.POST.get('contato')
        telefone = request.POST.get('telefone')
        curso = request.POST.get('curso')
        descricao = request.POST.get('mensagem')
        dia = datetime.today;

        assunto = "Descrição: \n" + descricao + "\nAutor: " + name + "\ncpf: " + cpf

        contact = ContactUs(name = name, email = email, cpf = cpf, course_name = curso, contact_type = contato, description = descricao)
        email = EmailMessage(curso, assunto, to=['roberto.matheus@bol.com.br'])
        email.send()

        return render_to_response('evl/home.html')
    else:
        form = ContactUsForm()
        return render(request, 'evl/fale_conosco.html', {'form': form})
