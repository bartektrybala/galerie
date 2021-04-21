from django.db import models

WIEK_OBIEKTU = (
    ('1', 'Bardzo Stary'),
    ('2', 'Stary+'),
    ('3', 'Średni'),
    ('4', 'Nowy'),
    ('5', 'Dopiero zbudowany (>rok)'),
)

WIELKOSC_OBIEKTU = (
    ('1', 'Bardzo mały'),
    ('2', 'Mały'),
    ('3', 'Średni'),
    ('4', 'Dość duży'),
    ('5', 'Duży'),
    ('6', 'Ogromny'),
)

STREFA_GASTRONOMICZNA = (
    ('1', 'Dobrze'),
    ('2', 'Dobrze+'),
    ('3', 'Dobrze++'),
    ('4', 'Źle'),
    ('5', 'Źle-'),
    ('6', 'Źle--'),
)

STREFA_WIZUALNA = (
    ('1', 'Dobrze'),
    ('2', 'Dobrze+'),
    ('3', 'Dobrze++'),
    ('4', 'Źle'),
    ('5', 'Źle-'),
    ('6', 'Źle--'),
)


class Galeria(models.Model):
    name = models.CharField(max_length=150)
    wielkosc_obiektu = models.CharField(choices=WIELKOSC_OBIEKTU, max_length=50)
    wiek_obiektu = models.CharField(choices=WIEK_OBIEKTU, max_length=50)
    obecnosc_hipermarketu = models.BooleanField()
    kino = models.BooleanField()
    kregielnia = models.BooleanField()
    strefa_dla_dzieci = models.BooleanField()
    przestrzen_gastronomiczna = models.CharField(choices=STREFA_GASTRONOMICZNA, max_length=50)
    strefa_wizualna = models.CharField(choices=STREFA_WIZUALNA, max_length=50)
    fryzjer = models.BooleanField()
    bankomat = models.BooleanField()
    bank = models.BooleanField()
    operator_komorkowy = models.BooleanField()
    lokalizacja = models.TextField()
    image = models.ImageField(default='building.png', upload_to='wspomaganie_decyzji/', null=True, blank=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=6)
