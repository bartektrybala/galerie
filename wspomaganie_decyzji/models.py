from django.db import models

ROZRYWKA = (
    ('1', 'Bardzo niski poziom'),
    ('2', 'Niski poziom'),
    ('3', 'Średni poziom'),
    ('4', 'Wysoki poziom'),
    ('5', 'Bardzo wysoki poziom'),
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
    ('1', 'Źle--'),
    ('2', 'Źle-'),
    ('3', 'Źle'),
    ('4', 'Dobrze'),
    ('5', 'Dobrze+'),
    ('6', 'Dobrze++'),
)

STREFA_WIZUALNA = (
    ('1', 'Źle--'),
    ('2', 'Źle-'),
    ('3', 'Źle'),
    ('4', 'Dobrze'),
    ('5', 'Dobrze+'),
    ('6', 'Dobrze++'),
)


class Galeria(models.Model):
    name = models.CharField(max_length=150)
    wielkosc_obiektu = models.CharField(choices=WIELKOSC_OBIEKTU, max_length=50)
    wyglad_obiektu = models.CharField(choices=STREFA_WIZUALNA, max_length=50)
    artykuly_spozywcze = models.CharField(choices=STREFA_GASTRONOMICZNA, max_length=50)
    rozrywka = models.CharField(choices=ROZRYWKA, max_length=50)
    uslugi = models.CharField(choices=ROZRYWKA, max_length=50)
    lokalizacja = models.TextField()
    image = models.ImageField(default='building.png', upload_to='wspomaganie_decyzji/', null=True, blank=True)

    def __str__(self):
        return self.name
