from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Galeria
import requests

from .forms import AddressForm, ChoiceForm1, ChoiceForm2
from .ahp import ahp_method, zbior
from .pass1 import YOUR_API_KEY


def distance(request):
    if request.method != 'POST':
        form = AddressForm()
    else:
        form = AddressForm(data=request.POST)
        global address
        address = request.POST['address'] + ', ' + request.POST['zip_code'] + ' ' + request.POST['city']

        return HttpResponseRedirect(reverse('wspomaganie_decyzji:ankieta'))
    context = {'form': form}
    return render(request, 'wspomaganie_decyzji/distance.html', context)


def ankieta(request):
    if request.method != 'POST':
        choices1 = ChoiceForm1()
        choices2 = ChoiceForm2()
    else:
        choices1 = ChoiceForm1(data=request.POST)
        choices2 = ChoiceForm2(data=request.POST)
        dict1 = list(dict(list(request.POST.items())[1:len(request.POST)//2+1]).values())
        dict2 = list(dict(list(request.POST.items())[len(request.POST)//2+1:]).values())

        weights = ahp_method(dict1, dict2)
        global C, CC, WW
        C = C_create()
        CC, WW = zbior(C, weights)
        return HttpResponseRedirect(reverse('wspomaganie_decyzji:ranking'))

    pola2 = Galeria._meta.get_fields()
    pola = pola2[2:8]
    A = []
    B = []
    for k, x in enumerate(pola):
        for y in pola[k:]:
            if x != y:
                A.append(x.name)
                B.append(y.name)

    context = {'A': A, 'B': B, 'choices1': choices1, 'choices2': choices2}
    return render(request, 'wspomaganie_decyzji/ankieta.html', context)


def ranking(request):
    C1 = sum(WW[0:6])
    C2 = sum(WW[7:13])
    C3 = sum(WW[14:20])
    C4 = sum(WW[21:27])
    C5 = sum(WW[28:34])
    C6 = sum(WW[35:41])
    C7 = sum(WW[42:48])
    C8 = sum(WW[49:55])

    D = {'1': C1, '2': C2, '3': C3, '4': C4, '5': C5, '6': C6, '7': C7, '8': C8}
    D = dict(sorted(D.items(), key=lambda item: item[1], reverse=True))

    galerie_ranking = [{}, {}, {}, {}, {}, {}, {}, {}]

    for i, d in enumerate(D):
        galeria = Galeria.objects.get(id=d)
        galerie_ranking[i]['name'] = galeria.name
        galerie_ranking[i]['image'] = galeria.image
        galerie_ranking[i]['wielkosc_obiektu'] = galeria.wielkosc_obiektu
        galerie_ranking[i]['wyglad_obiektu'] = galeria.wyglad_obiektu
        galerie_ranking[i]['artykuly_spozywcze'] = galeria.artykuly_spozywcze
        galerie_ranking[i]['rozrywka'] = galeria.rozrywka
        galerie_ranking[i]['uslugi'] = galeria.uslugi
        galerie_ranking[i]['dystans'] = str(G[int(d)-1][5]/1000) + ' km'

    context = {'galerie_ranking': galerie_ranking}
    return render(request, 'wspomaganie_decyzji/ranking.html', context)


def galerie(request):
    galerie = Galeria.objects.all()

    context = {'galerie': galerie}
    return render(request, 'wspomaganie_decyzji/galerie.html', context)


def galeria(request, galeria_id):
    galeria = Galeria.objects.get(id=galeria_id)

    context = {'galeria': galeria}
    return render(request, 'wspomaganie_decyzji/galeria.html', context)


def distanceMatrix(origin, destination):
    resp = requests.get(
        'https://maps.googleapis.com/maps/api/distancematrix/json?units-imperial&origins=' + origin + '&destinations=' + destination + '&key=' + YOUR_API_KEY)
    dist = resp.json()['rows'][0]['elements'][0]['distance']['value']
    return dist


def C_create():
    galerie = Galeria.objects.all()
    global G        # potrzebne do rankingu
    G = [[], [], [], [], [], [], [], []]
    for k, galeria in enumerate(galerie):
        G[k].append(galeria.wielkosc_obiektu)
        G[k].append(galeria.wyglad_obiektu)
        G[k].append(galeria.artykuly_spozywcze)
        G[k].append(galeria.rozrywka)
        G[k].append(galeria.uslugi)
        G[k].append(distanceMatrix(address, galeria.lokalizacja))

    C = {'C1': {'wielkosc_obiektu': '', 'wyglad_obiektu': '', 'artykuly_spozywcze': '', 'rozrywka': '', 'uslugi': '', 'odleglosc': ''},
         'C2': {'wielkosc_obiektu': '', 'wyglad_obiektu': '', 'artykuly_spozywcze': '', 'rozrywka': '', 'uslugi': '', 'odleglosc': ''},
         'C3': {'wielkosc_obiektu': '', 'wyglad_obiektu': '', 'artykuly_spozywcze': '', 'rozrywka': '', 'uslugi': '', 'odleglosc': ''},
         'C4': {'wielkosc_obiektu': '', 'wyglad_obiektu': '', 'artykuly_spozywcze': '', 'rozrywka': '', 'uslugi': '', 'odleglosc': ''},
         'C5': {'wielkosc_obiektu': '', 'wyglad_obiektu': '', 'artykuly_spozywcze': '', 'rozrywka': '', 'uslugi': '', 'odleglosc': ''},
         'C6': {'wielkosc_obiektu': '', 'wyglad_obiektu': '', 'artykuly_spozywcze': '', 'rozrywka': '', 'uslugi': '', 'odleglosc': ''},
         'C7': {'wielkosc_obiektu': '', 'wyglad_obiektu': '', 'artykuly_spozywcze': '', 'rozrywka': '', 'uslugi': '', 'odleglosc': ''},
         'C8': {'wielkosc_obiektu': '', 'wyglad_obiektu': '', 'artykuly_spozywcze': '', 'rozrywka': '', 'uslugi': '', 'odleglosc': ''}}
    for i, c in enumerate(C):
        C[c]['wielkosc_obiektu'] = G[i][0]
        C[c]['wyglad_obiektu'] = G[i][1]
        C[c]['artykuly_spozywcze'] = G[i][2]
        C[c]['rozrywka'] = G[i][3]
        C[c]['uslugi'] = G[i][4]
        C[c]['odleglosc'] = G[i][5]
    return C