# -*- coding: utf-8 -*-
from django import forms
from urllib.request import urlopen
import json

requisicao_categoria = urlopen("https://escolamodelows.interlegis.leg.br/api/v1/categorias_cursos")
response_categorias = json.load(requisicao_categoria)
categorias = response_categorias['categorias_cursos']
lista_categorias = [('-1', '-- Selecione uma categoria --')]
for categoria in categorias:
    if categoria['id'] != None:
        lista_categorias.append((categoria['id'], categoria['nome']))

lista_status = (('', '-- Selecione um estado --'), ('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado'))

class AvaliarCursosForm(forms.Form):
    status = forms.ChoiceField(
        choices = lista_status,
        widget = forms.Select(
            attrs={
                'class' : 'form-control',
                'onclick' : 'selectEstado()',
            }
        )
    )
    course_category_id = forms.ChoiceField(
        choices = lista_categorias,
        widget = forms.Select(
            attrs={
                'class' : 'form-control',
            }
        )
    )
    class Meta:
        fields = ('status', 'course_category_id')
