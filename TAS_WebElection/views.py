# -*- coding: UTF-8 -*- 

from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from voting.models import *


def home(request):
    errors = []
    candidates = []
    for cand in Kandydat.objects.all():
        candidates.append(
            {'id': cand.id, 'zdjecie': cand.zdjecie, 'imie': cand.imie, 'nazwisko': cand.nazwisko,
             'haslo': cand.haslo_wyborcze})

    if request.method == 'POST':
        if not request.POST.get('firstname', ''):
            errors.append(u'Wpisz imię!')
        if not request.POST.get('lastname', ''):
            errors.append(u'Wpisz nazwisko')
        if not request.POST.get('pesel', ''):
            errors.append(u'Wpisz pesel')
        if not request.POST.get('pass', ''):
            errors.append(u'Wpisz nr dowodu')

        if not errors:
            if verify_obywatel(request.POST['firstname'], request.POST['lastname'], request.POST['pesel'],
                               request.POST['pass']):
                add_vote(request.POST['candidate'])
            return HttpResponseRedirect('/vote/thanks')
    return render(request, 'main.html', {'lista_kandydatow': candidates, 'errors': errors})


def candidates(request):
    candidates = []
    for cand in Kandydat.objects.all():
        candidates.append(
            {'id': cand.id, 'zdjecie': cand.zdjecie, 'imie': cand.imie, 'nazwisko': cand.nazwisko,
             'haslo': cand.haslo_wyborcze, 'partia': cand.partia_id})
    return render_to_response('candidates.html', {'candidates': candidates})


def contact(request):
    return render_to_response('contact.html')


def verify_obywatel(firstname, lastname, pesel, dowod):
    try:
        Obywatel.objects.get(imie=firstname, nazwisko=lastname, PESEL=pesel, nr_dowodu=dowod)
    except Obywatel.DoesNotExist:
        return False
    else:
        return True


def add_vote(candidate):
    glos = Glos(kandydat=candidate)
    glos.save()
