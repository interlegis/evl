from django import forms
from .models import ContactUs
from urllib.request import urlopen
from localflavor.br.forms import BRCPFField
import json

requisicao_categoria = urlopen("https://escolamodelows.interlegis.leg.br/api/v1/categorias_cursos")
response_categorias = json.load(requisicao_categoria)
categorias = response_categorias['categorias_cursos']
lista_categorias = [('-1', '-- Selecione uma categoria --')]
for categoria in categorias:
    lista_categorias.append((categoria['id'], categoria['nome']))

requisicao_curso = urlopen("https://escolamodelows.interlegis.leg.br/api/v1/cursos")
response_cursos = json.load(requisicao_curso)
cursos = response_cursos['cursos']
lista_cursos = [('-1', '-- Selecione um curso --')]
for curso in cursos:
    lista_cursos.append((curso['id'], curso['nome']))

requisicao_escola = urlopen("http://escolamodelows.interlegis.leg.br/api/v1/escolas")
response_escolas = json.load(requisicao_escola)
escolas = response_escolas['escolas']
lista_escolas = [('-1', '-- Selecione uma escola --')]
for escola in escolas:
    lista_escolas.append((escola['initials'], escola['nome']))


lista_contatos = (('-1', '-- Selecione o tipo de contato --'), ('0', 'Reclamação'), ('1', 'Dúvida'), ('2', 'Sugestão'), ('3', 'Elogio'))

class ContactUsForm(forms.ModelForm):


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
                'class' : 'form-control',
                'placeholder' : 'CPF',
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
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Assunto',
            }
        )
    )
    course_id = forms.ChoiceField(
        choices = lista_cursos,
        widget = forms.Select(
            attrs={
                'class' : 'form-control',
            }
        )
    )
    school_initials = forms.ChoiceField(
        choices = lista_escolas,
        widget = forms.Select(
            attrs={
                'class' : 'form-control',
            }
        )
    )
    contact_type = forms.ChoiceField(
        choices = lista_contatos,
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
    description = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com a sua mensagem.'},
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Mensagem',
                'rows': '10',
                'cols': '50',
                'style': 'max-height: 400px;',
            }
        )
    )

    class Meta:
        model = ContactUs
        # fields = ('name', 'email', 'cpf', 'description',)
        fields = ('name', 'email', 'cpf', 'course_id', 'contact_type', 'course_category_id', 'description', 'school_initials')


    def clean_school_initials(self, *args, **kwargs):
        school_initials = self.cleaned_data.get("school_initials")
        if "-1" in school_initials:
            raise forms.ValidationError("Selecione uma escola")
        else:
            return school_initials

    def clean_course_id(self, *args, **kwargs):
        course_id = self.cleaned_data.get("course_id")
        if "-1" in course_id:
            raise forms.ValidationError("Selecione um curso")
        else:
            return course_id

    def clean_course_category_id(self, *args, **kwargs):
        course_category_id = self.cleaned_data.get("course_category_id")
        if "-1" in course_category_id:
            raise forms.ValidationError("Selecione uma categoria")
        else:
            return course_category_id

    def clean_contact_type(self, *args, **kwargs):
        contact_type = self.cleaned_data.get("contact_type")
        if "-1" in contact_type:
            raise forms.ValidationError("Selecione um tipo de contato")
        else:
            return contact_type
