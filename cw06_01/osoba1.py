def utworz_osobe(imie, nazwisko, wiek):
    return {
        'imie': imie,
        'nazwisko': nazwisko,
        'wiek': wiek
    }


# Dane wejściowe
osoba1 = utworz_osobe('Jan', 'Kowalski', 22)


def zmien_imie(osoba, imie):
    if imie:
        osoba['imie'] = imie
        print('Imię zostało zmienione...')
    else:
        # print('Błąd - imię nie może być puste!')
        raise ValueError('Imię nie może być puste!')


def zmien_nazwisko(osoba, nazwisko):
    if nazwisko:
        osoba['nazwisko'] = nazwisko
        print('Nazwisko zostało zmienione...')
    else:
        # print('Błąd - nazwisko nie może być puste!')
        raise ValueError('Nazwisko nie może być puste!')


def zmien_wiek(osoba, wiek):
    if 0 <= wiek <= 120:
        osoba['wiek'] = wiek
        print('Wiek został zmieniony...')
    else:
        # print('Błąd - nieprawidłowa liczba lat!')
        raise ValueError('Błędny wiek!')


def zmien_dane(osoba, imie, nazwisko, wiek):
    try:
        zmien_imie(osoba, imie)
    except ValueError as e:
        print(e)
    try:
        zmien_nazwisko(osoba, nazwisko)
    except ValueError as e:
        print(e)
    try:
        zmien_wiek(osoba, wiek)
    except (ValueError, TypeError) as e:
        print(e)


print(osoba1)
zmien_dane(osoba1, '', '', 130)
print(osoba1)
