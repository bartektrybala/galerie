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


class ChoiceForm1(forms.Form):
    field1a = forms.MultipleChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field2a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    fielda3a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    fielda4a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field5a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field6a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field7a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field8a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field9a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field10a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field11a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'integer',
               'class': 'form-control  mb-2'}
    ))
    field12a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field13a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field14a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field15a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))


class ChoiceForm2(forms.Form):
    field1b = forms.MultipleChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field2b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field3b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field4b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field5b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field6b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field7b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field8b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field9b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field10b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field11b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'integer',
               'class': 'form-control  mb-2'}
    ))
    field12b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field13b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field14b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))
    field15b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control  mb-2'}
    ))


