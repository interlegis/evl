# -*- coding: utf-8 -*-
from django import forms
from urllib.request import urlopen
# from localflavor.br.forms import BRCPFField
import json
from evl.models import User
from datetime import datetime
from django.contrib.auth.hashers import check_password

class PerfilForm(forms.Form):
    name = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o seu nome.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control enable_btn',
                'placeholder' : 'Nome',
                'disabled' : 'disabled',
            }
        )
    )
    email = forms.EmailField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o seu email.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control enable_btn',
                'placeholder' : 'Email',
                'disabled' : 'disabled',
            }
        )
    )
    # cpf = BRCPFField(
    cpf = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o seu cpf.'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control enable_btn',
                'placeholder': 'CPF',
                'disabled' : 'disabled',
            }
        )
    )
    phone = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o seu telefone.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control enable_btn',
                'placeholder' : 'Numero Celular',
                'disabled' : 'disabled',
            }
        )
    )

    birth_date = forms.CharField(
        label='Data de nascimento', 
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control enable_btn',
                'placeholder' : 'Data de Nascimento',
                'disabled' : 'disabled',
                'data-mask': "00/00/0000"
            }
        ))
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control enable_btn',
                'placeholder' : 'Senha',
                'disabled' : 'disabled',
            }
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control enable_btn',
                'placeholder' : 'Confirme a senha',
                'disabled' : 'disabled',
            }
        )
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PerfilForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(PerfilForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError(
                "Senha e confirmação de senha inválidas"
            )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            if self.user.email!=email:
                match = User.objects.get(email=email)
            else:
                return email
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Este email já está sendo utilizado.')

    def clean_birth_date(self):
        cleaned_data = super(PerfilForm, self).clean()
        birth_date = datetime.strptime(cleaned_data.get("birth_date"), '%d/%m/%Y')
        if datetime.now() <= birth_date or birth_date.year <= 1800:
            raise forms.ValidationError(u'Data inválida!')
        else:
            return birth_date