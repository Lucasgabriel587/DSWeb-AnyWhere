from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(
        'Disciplina: Desenvolvimento de Sistemas Web<br>'
        'Semestre: 2024.1<br>'
        'Matricula: 20211014040013<br>'
        'Nome: Lucas Gabriel'
    )