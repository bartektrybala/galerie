import ahpy

choice_comparisons = {('wielkosc_obiektu', 'wyglad_obiektu'): 4, ('wielkosc_obiektu', 'artykuly_spozywcze'): 3,
                      ('wielkosc_obiektu', 'rozrywka'): 1/2, ('wielkosc_obiektu', 'uslugi'): 5,
                      ('wielkosc_obiektu', 'lokalizacja'): 5,
                      ('wyglad_obiektu', 'artykuly_spozywcze'): 9, ('wyglad_obiektu', 'rozrywka'): 1/7,
                      ('wyglad_obiektu', 'uslugi'): 1/4, ('wyglad_obiektu', 'lokalizacja'): 1/4,
                      ('artykuly_spozywcze', 'rozrywka'): 5, ('artykuly_spozywcze', 'uslugi'): 6,
                      ('rozrywka', 'uslugi'): 7, ('rozrywka', 'lokalizacja'): 1/3,
                      ('uslugi', 'lokalizacja'): 1/7}

for count, i in enumerate(choice_comparisons):
    print(i, choice_comparisons[i], count)


def ahp_method(choices):
    for count, i in enumerate(choice_comparisons):
        if choices[count][0] > choices[count][1]:
            choice_comparisons[i] = choices[count][0]
        else:
            choice_comparisons[i] = 1/choices[count][0]

    ch = ahpy.Compare(name='Choices', comparisons=choice_comparisons, precision=3, random_index='saaty')
    return ch.target_weights
