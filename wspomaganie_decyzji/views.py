from django.shortcuts import render
from .models import Galeria
import requests

YOUR_API_KEY = 'AIzaSyC4w8YmL6ETYnjZ6XYNyoVovktUhDZRRmI'


def index(request):
    origins = 'Wrocław'
    destinations = 'Warszawa'


    resp = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?units-imperial&origins='+origins+'&destinations='+destinations+'&key='+ YOUR_API_KEY)
    distance = resp.json()
    context = {'distance': distance}
    return render(request, 'wspomaganie_decyzji/index.html', context)


def galerie(request):
    galerie = Galeria.objects.all()

    context = {'galerie': galerie}
    return render(request, 'wspomaganie_decyzji/galerie.html', context)


def galeria(request, galeria_id):
    galeria = Galeria.objects.get(id=galeria_id)

    origins = 'Lutynia, 55-330'
    destinations = galeria.lokalizacja

    resp = requests.get(
        'https://maps.googleapis.com/maps/api/distancematrix/json?units-imperial&origins=' + origins + '&destinations=' + destinations + '&key=' + YOUR_API_KEY)
    origin = resp.json()['origin_addresses'][0]
    distance = resp.json()['rows'][0]['elements'][0]['distance']['text']

    context = {'galeria': galeria, 'distance': distance, 'origin': origin}
    return render(request, 'wspomaganie_decyzji/galeria.html', context)
