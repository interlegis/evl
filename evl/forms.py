# -*- coding: utf-8 -*-
from django import forms
from urllib.request import urlopen
from localflavor.br.forms import BRCPFField
import json

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
    cpf = BRCPFField(
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

    birth_date = forms.DateField(
        label='Data de nascimento', 
        widget=forms.SelectDateWidget(
            attrs={
                'class' : 'enable_btn',
                'placeholder' : 'Data de Nascimento',
                'disabled' : 'disabled',
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

    def clean(self):
        cleaned_data = super(PerfilForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Senha e confirmação de senha inválidas"
            )