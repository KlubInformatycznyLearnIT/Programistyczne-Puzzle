def pobierzLiczbe():
    return int(input("Podaj liczbę do sprawdzenia: "))

def liczbaPierwsza(liczba):
    pierwsza = czyPierwsza(liczba)
    if pierwsza:
        opis = ""
    else:
        opis = "nie "
    print("{} {}jest liczbą pierwszą.".format(liczba, opis))

def czyPierwsza(liczba):
    if liczba == 1:
        pierwsza = False
    elif liczba == 2:
        pierwsza = True
    else:
        pierwsza = True
        #największym możliwym dzielnikiem liczby, która nie jest pierwsza, jest jej połowa
        #więc: dla 100 największym dzielnikiem jest 50, dla 72 jest 36, itd.
        for dzielnik in range(2, int((liczba / 2)+1)):
            if liczba % dzielnik == 0:
                pierwsza = False
                break
    return pierwsza

#nieskończona pętla do sprawdzania liczb pierwszych
#while True:
#    liczbaPierwsza(pobierzLiczbe())
