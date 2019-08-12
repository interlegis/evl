from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^cursos/$', views.cursos, name='cursos'),
    url(r'^meuscursos/', views.meusCursos, name='meusCursos'),
    url(r'^baseCursos', views.baseCursos, name='baseCursos'),
    url(r'^registro_curso/', views.registroCurso, name='registroCurso'),
]
