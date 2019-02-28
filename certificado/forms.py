# -*- coding: utf-8 -*-
from django import forms

class ValidarCertificadoForm(forms.Form):
    code_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Código do certificado',
                'class': 'text-center, form-control',
                'style': 'text-align: center !important;'
            }
        )
    )
