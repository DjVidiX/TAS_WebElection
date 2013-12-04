# -*- coding: UTF-8 -*- 

from django.shortcuts import render_to_response
from voting.models import *
from django.shortcuts import render
from TAS_WebElection.forms import ContactForm
from django.core.mail import send_mail


def home(request):
    errors = []
    candidates = []
    message = ''

    if request.method == 'POST':
        if not request.POST.get('firstName', ''):
            errors.append(u'Wpisz imię!')
        if not request.POST.get('lastName', ''):
            errors.append(u'Wpisz nazwisko')
        if not request.POST.get('pesel', ''):
            errors.append(u'Wpisz pesel')
        if not request.POST.get('pass', ''):
            errors.append(u'Wpisz nr dowodu')

        if not errors:
            if verify_obywatel(request.POST['firstName'], request.POST['lastName'], request.POST['pesel'],
                               request.POST['pass']):
                add_vote(request.POST['candidate'])
                message = "Dziękujemy za twój głos!"
            else:
                errors.append("Nie jestes na liscie uprawnionych do glosowania")

    for cand in Kandydat.objects.all():
        try:
            l = Glos.objects.filter(kandydat=cand)
        except Glos.DoesNotExist:
            l = []

        candidates.append(
            {'id': cand.id, 'zdjecie': cand.zdjecie, 'imie': cand.imie, 'nazwisko': cand.nazwisko,
             'haslo': cand.haslo_wyborcze, 'glosy': len(l)})

    return render(request, 'main.html', {'lista_kandydatow': candidates, 'errors': errors, 'message': message})


def candidates(request):
    candidates = []
    for cand in Kandydat.objects.all():
        candidates.append(
            {'id': cand.id, 'zdjecie': cand.zdjecie, 'imie': cand.imie, 'nazwisko': cand.nazwisko,
             'haslo': cand.haslo_wyborcze, 'partia': cand.partia, 'wiek': cand.wiek})
    return render_to_response('candidates.html', {'candidates': candidates})


def contact(request):
    message = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['tytul'],
                cd['wiadomosc'],
                cd.get('email'),
                ['sterenczak.marek@gmail.com'],
            )
            message = "Dziękujemy za twoja opinie!"
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'message': message})


def verify_obywatel(firstName, lastName, pesel, dowod):
    try:
        o = Obywatel.objects.get(imie=firstName, nazwisko=lastName, PESEL=pesel, nr_dowodu=dowod, glosowal=False)
        o.glosowal = True
        o.save()
        return True
    except Obywatel.DoesNotExist:
        return False


def add_vote(candidate):
    kandydat = Kandydat.objects.get(id=candidate)
    glos = Glos(kandydat=kandydat)
    glos.save()
