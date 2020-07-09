from django.shortcuts import render
from core.models import Evento

# Create your views here.

# def index(request):
#   return redirect('/agenda/')

def lista_eventos(resquest):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(resquest, 'agenda.html', dados)

