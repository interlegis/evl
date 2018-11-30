from django.conf.urls import url
from django.urls import include
from . import views

urlpatterns = [
   url(r'^comprovantes/', views.comprovantes, name='comprovantes'),
]
