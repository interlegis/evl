"""evl_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^cursos/$', views.cursos, name='cursos'),
    url(r'^faleConosco/$', views.faleConosco, name='faleConosco'),
    url(r'^faleConoscoMensagens/$', views.mensagensFaleConosco, name='mensagensFaleConosco'),
    url(r'^cadastro/$', views.cadastro, name='cadastro'),
    url(r'^cursosPendentes/(?P<id>\d+)/avaliarCursos/', views.avaliarCursos, name='avaliarCursos'),
    url(r'^cursosPendentes/$', views.cursosPendentes, name='cursosPendentes'),
    url(r'^meuscursos/', views.meusCursos, name='meusCursos'),
    url(r'^certificados/', views.certificados, name='certificados'),
    url(r'^validarCertificado/', views.validarCertificado, name='validarCertificado'),
    url(r'^comprovantes/', views.comprovantes, name='comprovantes'),
    url(r'^aluno', views.homeAluno, name='homealuno'),
    url(r'^baseCursos', views.baseCursos, name='baseCursos'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^secret$', views.secret_page, name='secret'),
   # url(r'^accounts/login/$', views.loginOAuth, name="loginOAuth")
]
