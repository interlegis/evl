from django.shortcuts import render
import requests
import json



def adesao_institucional(request):
    adesao_institucional = requests.get('http://localhost:3000/api/v1/escolas?key=k4B5YcbKa619ohu3wxk2xXbmtoxFuQqrwcKEOTAnZi7iy4tl9z')
    escolas = json.loads(adesao_institucional.content)
    return render(request, 'adesao_institucional.html', {'escolas': escolas})



def meusCursos(request):
    user_cursos = requests.get('http://localhost:3000/api/v1/cursos?key=k4B5YcbKa619ohu3wxk2xXbmtoxFuQqrwcKEOTAnZi7iy4tl9z')
    cursos = json.loads(user_cursos.content)
    return render(request, 'meusCursos.html', {'cursos': cursos})