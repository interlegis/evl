from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^faleConosco/$', views.faleConosco, name='faleConosco'),
    url(r'^faleConoscoMensagens/$', views.mensagensFaleConosco, name='mensagensFaleConosco'),
]
