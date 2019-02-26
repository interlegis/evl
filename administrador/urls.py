from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^administrador/$', views.administrador, name='administrador'),
    url(r'^cursosPendentes/$', views.cursosPendentes, name='cursosPendentes'),
    url(r'^categoriasGestao/$', views.categoriasGestao, name='categoriasGestao'),
    url(r'^aprovar_curso/(?P<curso>\d+)/(?P<categoria>\d+)/$', views.aprovar_curso, name='aprovar_curso'),
    url(r'^reprovar_curso/(?P<curso>\d+)/(?P<categoria>\d+)/$', views.reprovar_curso, name='reprovar_curso'),
    url(r'^editar_categoria/(?P<categoria>\d+)/(?P<nome>.+?)/$', views.editar_categoria, name='editar_categoria'),
    url(r'^criar_categoria/(?P<nome>.+?)/$', views.criar_categoria, name='criar_categoria'),
]
