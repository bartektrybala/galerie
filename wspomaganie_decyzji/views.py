from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Galeria
import requests

from .forms import AddressForm, ChoiceForm

YOUR_API_KEY = 'AIzaSyC4w8YmL6ETYnjZ6XYNyoVovktUhDZRRmI'


def distance(request):
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
        return render(request, 'wspomaganie_decyzji/distance.html', context)
    context = {'form': form, 'distance': distance}
    return render(request, 'wspomaganie_decyzji/distance.html', context)


def trala(dict):
    A = []
    for i in dict:
        if i != 'csrfmiddlewaretoken':
            print(dict[i])
    return A


def index(request):
    if request.method != 'POST':
        choices = ChoiceForm()
    else:
        choices = ChoiceForm(data=request.POST)
        dict = request.POST.items
        print(dict)
        #dict = trala(request.POST)
        #print(dict)
        return HttpResponseRedirect(reverse(('wspomaganie_decyzji:index')))

    pola2 = Galeria._meta.get_fields()
    pola = pola2[2:8]
    A = []
    B = []
    for k, x in enumerate(pola):
        for y in pola[k:]:
            if x != y:
                A.append(x.name)
                B.append(y.name)
    context = {'A': A, 'B': B, 'choices': choices}
    return render(request, 'wspomaganie_decyzji/index.html', context)


def galerie(request):
    galerie = Galeria.objects.all()

    context = {'galerie': galerie}
    return render(request, 'wspomaganie_decyzji/galerie.html', context)


def galeria(request, galeria_id):
    galeria = Galeria.objects.get(id=galeria_id)

    origins = 'Tadeusza Kościuszki 13, Wrocław'
    destinations = galeria.lokalizacja

    distance = distanceMatrix(origins, destinations)

    context = {'galeria': galeria, 'distance': distance, 'origin': origins}
    return render(request, 'wspomaganie_decyzji/galeria.html', context)


def distanceMatrix(origin, destination):
    resp = requests.get(
        'https://maps.googleapis.com/maps/api/distancematrix/json?units-imperial&origins=' + origin + '&destinations=' + destination + '&key=' + YOUR_API_KEY)
    dist = resp.json()['rows'][0]['elements'][0]['distance']['text']
    return dist