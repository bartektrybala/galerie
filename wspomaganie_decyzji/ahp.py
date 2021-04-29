import ahpy

choice_comparisons = {('wielkosc_obiektu', 'wyglad_obiektu'): 4, ('wielkosc_obiektu', 'artykuly_spozywcze'): 3,
                      ('wielkosc_obiektu', 'rozrywka'): 1/2, ('wielkosc_obiektu', 'uslugi'): 5,
                      ('wielkosc_obiektu', 'lokalizacja'): 5,
                      ('wyglad_obiektu', 'artykuly_spozywcze'): 9, ('wyglad_obiektu', 'rozrywka'): 1/7,
                      ('wyglad_obiektu', 'uslugi'): 1/4, ('wyglad_obiektu', 'lokalizacja'): 1/4,
                      ('artykuly_spozywcze', 'rozrywka'): 5, ('artykuly_spozywcze', 'uslugi'): 6,
                      ('rozrywka', 'uslugi'): 7, ('rozrywka', 'lokalizacja'): 1/3,
                      ('uslugi', 'lokalizacja'): 1/7}


def ahp_method(dict1, dict2):
    for count, i in enumerate(choice_comparisons):
        if dict1[count] > dict2[count]:
            choice_comparisons[i] = int(dict1[count])
        else:
            choice_comparisons[i] = 1/int(dict2[count])

    ch = ahpy.Compare(name='Choices', comparisons=choice_comparisons, precision=3, random_index='saaty')
    return ch.target_weights


def zbior(C, weights):
    CC = []     # porównanie wariantów
    WW = []      # suma ważności kryteriów, których numery trafiły do CC
    for c1 in C:
        for c2 in C:
            if c1 != c2:
                X = {}
                w_sum = 0           # suma ważności dla każdego porównania
                for i, cc1 in enumerate(C[c1]):
                    if C[c1][cc1] < C[c2][cc1] and cc1 != 'odleglosc':
                        continue
                    elif C[c1][cc1] >= C[c2][cc1] and cc1 != 'odleglosc':
                        X[cc1] = C[c1][cc1]
                        w_sum += weights[cc1]
                    elif C[c1][cc1] > C[c2][cc1] and cc1 == 'odleglosc':
                        continue
                    elif C[c1][cc1] <= C[c2][cc1] and cc1 == 'odleglosc':
                        X[cc1] = C[c1][cc1]
                        w_sum += weights['lokalizacja']
                w_sum = round(w_sum, 2)
                CC.append(X)
                WW.append(w_sum)
    return CC, WW
