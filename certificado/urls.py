from django.conf.urls import url
from django.urls import include
from . import views

urlpatterns = [
    url(r'^certificados/', views.certificados, name='certificados'),
    url(r'^validarCertificado/', views.validarCertificado, name='validarCertificado'),
]
