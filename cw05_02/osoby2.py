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
        print('Błąd - imię nie może być puste!')


def zmien_nazwisko(osoba, nazwisko):
    if nazwisko:
        osoba['nazwisko'] = nazwisko
        print('Nazwisko zostało zmienione...')
    else:
        print('Błąd - nazwisko nie może być puste!')


def zmien_wiek(osoba, wiek):
    if 0 <= wiek <= 120:
        osoba['wiek'] = wiek
        print('Wiek został zmieniony...')
    else:
        print('Błąd - nieprawidłowa liczba lat!')


def zmien_dane(osoba, imie, nazwisko, wiek):
    zmien_imie(osoba, imie)
    zmien_nazwisko(osoba, nazwisko)
    zmien_wiek(osoba, wiek)

print(osoba1)
zmien_dane(osoba1, '', '', 130)
print(osoba1)
