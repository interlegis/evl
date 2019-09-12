# -*- coding: utf-8 -*-
from django import forms
from evl.models import User
from datetime import datetime
import requests
import json
from django.conf import settings

response_quiz = requests.get(settings.BASE_URL + 'cursos/registro?id=1&key=' + settings.APIKEY) # TODO alterar para chave do usuário
quiz = json.loads(response_quiz.content)


class RegistroForm(forms.Form):

    quiz = quiz.quiz

    name = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o seu nome.'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control enable_btn',
                'placeholder': 'Nome',
                'disabled': 'disabled',
            }
        )
    )