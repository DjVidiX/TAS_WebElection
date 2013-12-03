# -*- coding: UTF-8 -*- 

from TAS_WebElection.views import *
from voting.models import Kandydat

def home(request):
    candidates = []
    for cand in Kandydat.objects.all():
        candidates.append(
            {'zdjecie': cand.zdjecie, 'imie': cand.imie, 'nazwisko': cand.nazwisko, 'haslo': cand.haslo_wyborcze})
    return render_to_response('main.html', {'lista_kandydatow': candidates})


def candidates(request):
    lista = ['Marek', 'Lukasz']
    return render_to_response('candidates.html', {'listahtml': lista})


def vote(request):
    return render_to_response('vote.html')


def index(request):
    return render_to_response('index.html')
