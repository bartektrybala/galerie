from django import forms

from .models import Address

GALERIE = (
    ('1', 'Magnolia Park'),
    ('2', 'Wroclavia'),
    ('3', 'Pasaż Grunwaldzki'),
    ('4', 'Galeria Dominikańska'),
    ('5', 'Centrum Handlowe Korona'),
    ('6', 'Aleja Bielany'),
    ('7', 'Sky Tower'),
    ('8', 'Arkady Wrocławskie'),
)


class AddressForm(forms.Form):
    address = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Białowieska 3/15',
               'type': 'text',
               'class': 'form-control',
               'id': 'inputAddress'}))
    city = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'inputCity',
               'placeholder': 'Wrocław'}))
    zip_code = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'inputZip',
               'placeholder': '54-201'}
    ))
    galeria = forms.ChoiceField(choices=GALERIE, widget=forms.Select(
        attrs={'class': 'form-control',
               'id': 'inputGaleria'}
    ))
