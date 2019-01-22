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
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.userLogout, name='user_logout'),
    url(r'^cadastro/$', views.cadastro, name='cadastro'),
    url(r'^aluno', views.homeAluno, name='homealuno'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^secret$', views.secret_page, name='secret'),
    path('', include('cursos.urls')),
    path('', include('fale_conosco.urls')),
    path('', include('certificado.urls')),
    path('', include('comprovante.urls')),
    path('', include('administrador.urls')),
    url(r'^oidc/', include('mozilla_django_oidc.urls')),
   # url(r'^accounts/login/$', views.loginOAuth, name="loginOAuth")
]
