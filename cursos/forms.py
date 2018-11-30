# -*- coding: utf-8 -*-
from django import forms

class AvaliarCursosForm(forms.Form):
    status = forms.ChoiceField(
        choices = lista_status,
        widget = forms.Select(
            attrs={
                'class' : 'form-control',
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
