from django.conf import settings
from django.shortcuts import render
import requests
import json



def adesao_institucional(request):
    adesao_institucional = requests.get(settings.BASE_URL + 'api/v1/escolas?key=' + settings.APIKEY)
    escolas = json.loads(adesao_institucional.content)
    return render(request, 'adesao_institucional.html', {'escolas': escolas})