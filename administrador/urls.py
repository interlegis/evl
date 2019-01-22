from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^administrador/$', views.administrador, name='administrador'),
    url(r'^cursosPendentes/$', views.cursosPendentes, name='cursosPendentes'),
    url(r'^aprovar_curso/(?P<curso>\d+)/(?P<categoria>\d+)/$', views.aprovar_curso, name='aprovar_curso'),
    url(r'^reprovar_curso/(?P<curso>\d+)/(?P<categoria>\d+)/$', views.reprovar_curso, name='reprovar_curso'),
]
