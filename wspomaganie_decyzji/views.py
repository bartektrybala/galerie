from django.shortcuts import render
from .models import Galeria


def index(request):
    return render(request, 'wspomaganie_decyzji/index.html')


def galerie(request):
    galerie = Galeria.objects.all()

    context = {'galerie': galerie}
    return render(request, 'wspomaganie_decyzji/galerie.html', context)


def galeria(request, galeria_id):
    galeria = Galeria.objects.get(id=galeria_id)

    context = {'galeria': galeria}
    return render(request, 'wspomaganie_decyzji/galeria.html', context)
