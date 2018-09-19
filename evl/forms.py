from django import forms
from .models import ContactUs, Courses
from urllib.request import urlopen
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

lista_contatos = (('C1', '-- Selecione o tipo de contato --'), ('C1', 'Reclamação'), ('C2', 'Dúvida'), ('C3', 'Sugestão'), ('C4', 'Elogio'))

class ContactUsForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Nome',
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Email',
        }
    ))
    cpf = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'CPF',
        }
    ))
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Numero Celular',
        }
    ))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Assunto',
        }
    ))
    course_name = forms.ChoiceField(
        choices = lista_cursos,
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
    course_category = forms.ChoiceField(
        choices = lista_categorias,
        widget = forms.Select(
            attrs={
                'class' : 'form-control',
            }
        )
    )
    description = forms.CharField(
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
        fields = ('name', 'email', 'cpf', 'course_name', 'contact_type', 'course_category', 'description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course_category'].queryset = Courses.objects.none()
