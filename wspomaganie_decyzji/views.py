from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Galeria
import requests

from .forms import AddressForm

YOUR_API_KEY = 'AIzaSyC4w8YmL6ETYnjZ6XYNyoVovktUhDZRRmI'


def index(request):
    distance = ''
    if request.method != 'POST':
        form = AddressForm()
    else:
        form = AddressForm(data=request.POST)
        address = request.POST['address'] + ', ' + request.POST['zip_code'] + ' ' + request.POST['city']
        gal_id = request.POST['galeria']
        galeria = Galeria.objects.get(id=gal_id)

        distance = distanceMatrix(address, galeria.lokalizacja)
        context = {'form': form, 'distance': distance}
        return render(request, 'wspomaganie_decyzji/index.html', context)
    context = {'form': form, 'distance': distance}
    return render(request, 'wspomaganie_decyzji/index.html', context)


def galerie(request):
    galerie = Galeria.objects.all()

    context = {'galerie': galerie}
    return render(request, 'wspomaganie_decyzji/galerie.html', context)


def galeria(request, galeria_id):
    galeria = Galeria.objects.get(id=galeria_id)

    origins = 'Lutynia, 55-330'
    destinations = galeria.lokalizacja

    distance = distanceMatrix(origins, destinations)

    context = {'galeria': galeria, 'distance': distance, 'origin': origins}
    return render(request, 'wspomaganie_decyzji/galeria.html', context)


def distanceMatrix(origin, destination):
    resp = requests.get(
        'https://maps.googleapis.com/maps/api/distancematrix/json?units-imperial&origins=' + origin + '&destinations=' + destination + '&key=' + YOUR_API_KEY)
    dist = resp.json()['rows'][0]['elements'][0]['distance']['text']
    return dist