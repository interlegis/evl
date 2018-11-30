# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import xlsxwriter
import requests
import json
from .models import *
import urllib.parse
import urllib.request
from django.http.response import HttpResponse


def comprovantes(request):
    return render(request, 'comprovantes.html')
