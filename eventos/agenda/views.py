from multiprocessing import context
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

from agenda.models import Evento

# Create your views here.
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(
        request=request,
        context={'eventos': eventos},
        template_name='agenda/listar_eventos.html'
    )

def exibir_evento(request, id):
    evento = {
        'nome': 'Teste',
        'categoria': 'Categoria A',
        'local': 'São Paulo'
    }
    return render(request=request, context={'evento': evento}, template_name='agenda/exibir_evento.html')

    