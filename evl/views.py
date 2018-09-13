# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect,get_object_or_404
import xlsxwriter
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers

def home(request):
    return render(request, 'evl/home.html')

def cursos(request):
    cursos = Courses.objects.all()
    cursos_json = serializers.serialize("json", cursos)
    categorias = CourseCategories.objects.all()
    return render(request, 'evl/cursos.html', {'cursos' : cursos, 'categorias' : categorias, 'cursos_json' : cursos_json})
