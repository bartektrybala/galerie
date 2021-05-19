from django import forms

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
    field1a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field2a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field3a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field4a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field5a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field6a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field7a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field8a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field9a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field10a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field11a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'integer',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field12a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field13a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field14a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field15a = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))


class ChoiceForm2(forms.Form):
    field1b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field2b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field3b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field4b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field5b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field6b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field7b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field8b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field9b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field10b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field11b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'integer',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field12b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field13b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field14b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))
    field15b = forms.ChoiceField(choices=OCENY, widget=forms.Select(
        attrs={'type': 'text',
               'class': 'form-control mb-2',
               'onchange': "myFunction(this);"}
    ))


