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

OCENY = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
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


class ChoiceForm(forms.Form):
    field1 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control btn-lg mb-2'}
    ))
    field2 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control btn-lg mb-2'}
    ))
    field3 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control btn-lg mb-2'}
    ))
    field4 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control btn-lg mb-2'}
    ))
    field5 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control btn-lg mb-2'}
    ))
    field6 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control btn-lg mb-2'}
    ))
    field7 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control btn-lg mb-2'}
    ))
    field8 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control btn-lg mb-2'}
    ))
    field9 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control btn-lg mb-2'}
    ))
    field10 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control btn-lg mb-2'}
    ))
    field11 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'integer',
               'class': 'form-control btn-lg mb-2'}
    ))
    field12 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control btn-lg mb-2'}
    ))
    field13 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control btn-lg mb-2'}
    ))
    field14 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control btn-lg mb-2'}
    ))
    field15 = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control btn-lg mb-2'}
    ))


