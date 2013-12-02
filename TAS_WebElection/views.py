from django.shortcuts import render_to_response
from TAS_WebElection.views import *
from voting.models import Kandydat

def home(request):
    candidates = []
    for cand in Kandydat.objects.all():
        candidates.append({'zdjecie':cand.zdjecie, 'imie':cand.imie, 'nazwisko':cand.nazwisko}) 
    return render_to_response('main.html', {'lista_kandydatow': candidates})


def candidates(request):
    lista = ['Marek', 'Lukasz']
    return render_to_response('candidates.html', {'listahtml': lista})


def vote(request):
    return render_to_response('vote.html')


def index(request):
    return render_to_response('index.html')
