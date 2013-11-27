from django.shortcuts import render_to_response


def home(request):
    return render_to_response('main.html')


def candidates(request):
    lista = ['Marek', 'Lukasz']
    return render_to_response('candidates.html', {'listahtml': lista})


def vote(request):
    return render_to_response('vote.html')


def index(request):
    return render_to_response('index.html')
