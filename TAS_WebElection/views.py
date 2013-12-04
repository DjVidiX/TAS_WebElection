# -*- coding: UTF-8 -*- 

from django.shortcuts import render_to_response
from voting.models import Kandydat


def home(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'

    candidates = []
    for cand in Kandydat.objects.all():
        candidates.append(
            {'zdjecie': cand.zdjecie, 'imie': cand.imie, 'nazwisko': cand.nazwisko, 'haslo': cand.haslo_wyborcze})
    return render_to_response('main.html', {'lista_kandydatow': candidates, 'message': message})


def candidates(request):
    lista = ['Marek', 'Lukasz']
    return render_to_response('candidates.html', {'listahtml': lista})


def contact(request):
    return render_to_response('contact.html')
