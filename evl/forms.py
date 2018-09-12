from django import forms
from .models import

class ContactUsForm(forms.ModelForm):

    class Meta:
        model = FaleConosco
        fields = ('name', 'email', 'cpf', 'course_name', 'contact_type', 'description',)
