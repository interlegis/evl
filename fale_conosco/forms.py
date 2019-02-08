# -*- coding: utf-8 -*-
from django import forms
from urllib.request import urlopen
from localflavor.br.forms import BRCPFField
import json

requisicao_categoria = urlopen("http://localhost:3000/api/v1/categorias_cursos?key=k4B5YcbKa619ohu3wxk2xXbmtoxFuQqrwcKEOTAnZi7iy4tl9z")
response_categorias = json.load(requisicao_categoria)
categorias = response_categorias['categorias_cursos']
lista_categorias = [('-1', 'Selecione uma categoria')]
for categoria in categorias:
    if categoria['id'] != None:
        lista_categorias.append((categoria['id'], categoria['nome']))

requisicao_curso = urlopen("http://localhost:3000/api/v1/cursos?key=k4B5YcbKa619ohu3wxk2xXbmtoxFuQqrwcKEOTAnZi7iy4tl9z")
response_cursos = json.load(requisicao_curso)
cursos = response_cursos['cursos']
lista_cursos = [('-1', 'Selecione um curso')]
for curso in cursos:
    if curso['id'] != None:
        lista_cursos.append((curso['id'], curso['nome']))

requisicao_escola = urlopen("http://localhost:3000/api/v1/escolas?key=k4B5YcbKa619ohu3wxk2xXbmtoxFuQqrwcKEOTAnZi7iy4tl9z")
response_escolas = json.load(requisicao_escola)
escolas = response_escolas['escolas']
lista_escolas = [('-1', 'Selecione uma escola')]
for escola in escolas:
    if escola['initials'] != None:
        lista_escolas.append((escola['initials'], escola['nome']))


lista_contatos = (('-1', 'Selecione o tipo de contato'), ('0', 'Reclamação'), ('1', 'Dúvida'), ('2', 'Sugestão'), ('3', 'Elogio'))

class FaleConoscoForm(forms.Form):
    name = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o seu nome.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Nome',
            }
        )
    )

    email = forms.EmailField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o seu email.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Email',
            }
        )
    )
    cpf = BRCPFField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o seu cpf.'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'CPF',

            }
        )
    )
    forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'CPF',
        }
    ))
    phone_number = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o seu telefone.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Numero Celular',
            }
        )
    )
    course_id = forms.ChoiceField(
        choices = lista_cursos,
        widget = forms.Select(
            attrs={
                'class' : 'custom-select',
            }
        )
    )
    school_initials = forms.ChoiceField(
        error_messages={'required': 'Este campo é obrigatório! Escolha a sua escola.'},
        choices = lista_escolas,
        widget = forms.Select(
            attrs={
                'class' : 'custom-select',
            }
        )
    )
    type_conversation = forms.ChoiceField(
        choices = lista_contatos,
        widget = forms.Select(
            attrs={
                'class' : 'custom-select',
            }
        )
    )
    course_category_id = forms.ChoiceField(
        choices = lista_categorias,
        widget = forms.Select(
            attrs={
                'class' : 'custom-select',
            }
        )
    )
    description = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com a sua mensagem.'},
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Mensagem',
                'rows': '10',
                'cols': '50',
                'style': 'max-height: 400px; min-height: 50px',
            }
        )
    )
    title = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o título.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Título',
            }
        )
    )

    class Meta:
        fields = ('name', 'email', 'cpf', 'course_id', 'type_conversation', 'course_category_id', 'title', 'description', 'school_initials')

    def clean_school_initials(self, *args, **kwargs):
        school_initials = self.cleaned_data.get("school_initials")
        print("INICIAIS = ", school_initials)
        if "-1" in school_initials:
            raise forms.ValidationError("Este campo é obrigatório! Selecione uma escola.")
        else:
            return school_initials

    def clean_type_conversation(self, *args, **kwargs):
        type_conversation = self.cleaned_data.get("type_conversation")
        if "-1" in type_conversation:
            raise forms.ValidationError("Este campo é obrigatório! Selecione um tipo de contato.")
        else:
            return type_conversation

class FaleConoscoFormLogged(forms.Form):
    name = forms.CharField(
        required = False,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Nome',
            }
        )
    )

    email = forms.EmailField(
        required = False,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Email',
            }
        )
    )
    cpf = BRCPFField(
        required = False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'CPF',

            }
        )
    )
    forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'CPF',
        }
    ))
    phone_number = forms.CharField(
        required = False,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Numero Celular',
            }
    ))
    course_id = forms.ChoiceField(
        choices = lista_cursos,
        widget = forms.Select(
            attrs={
                'class' : 'custom-select',
            }
        )
    )
    school_initials = forms.ChoiceField(
        error_messages={'required': 'Este campo é obrigatório! Escolha a sua escola.'},
        choices = lista_escolas,
        widget = forms.Select(
            attrs={
                'class' : 'custom-select',
            }
        )
    )
    type_conversation = forms.ChoiceField(
        choices = lista_contatos,
        widget = forms.Select(
            attrs={
                'class' : 'custom-select',
            }
        )
    )
    course_category_id = forms.ChoiceField(
        choices = lista_categorias,
        widget = forms.Select(
            attrs={
                'class' : 'custom-select',
            }
        )
    )
    description = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com a sua mensagem.'},
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Mensagem',
                'rows': '10',
                'cols': '50',
                'style': 'max-height: 400px; min-height: 50px',
            }
        )
    )
    title = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o título.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Título',
            }
        )
    )

    class Meta:
        fields = ('course_id', 'type_conversation', 'course_category_id', 'title', 'description', 'school_initials')

    def clean_school_initials(self, *args, **kwargs):
        school_initials = self.cleaned_data.get("school_initials")
        print("INICIAIS = ", school_initials)
        if "-1" in school_initials:
            raise forms.ValidationError("Este campo é obrigatório! Selecione uma escola.")
        else:
            return school_initials

    def clean_type_conversation(self, *args, **kwargs):
        type_conversation = self.cleaned_data.get("type_conversation")
        if "-1" in type_conversation:
            raise forms.ValidationError("Este campo é obrigatório! Selecione um tipo de contato.")
        else:
            return type_conversation
