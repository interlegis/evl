from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        # fields = ('name', 'email',)
        fields = ('name', 'email', 'cpf', 'course_name', 'contact_type', 'description',)
