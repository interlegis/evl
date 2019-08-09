from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^certificados/', views.certificados, name='certificados'),
    url(r'^validarCertificado/$', views.validarCertificado, name='validarCertificado'),
    url(r'^pdf/$', views.pdf, name='pdf'),
    path('validarCertificado/<code>', views.validacaoQrCode, name='validacao_qrcode'),
]
