#PRZYKŁADOWA LISTA
lista = [0,10,12,1,54,342,2,5,7,43,2,1264,3147,11,1243,54,6,7]

#ZAD 2
def mniejszeOd10(lista):
    nowaLista = []

    for liczba in lista:
        if liczba < 10:
            nowaLista.append(liczba)

    nowaLista.sort(reverse=True) #reverse=True -> sortowanie od największej do najmniejszej
    return nowaLista

print(mniejszeOd10(lista))

#ZAD 2.1
def mniejszeOd10String(lista):
    nowaLista = []

    for liczba in lista:
        if liczba < 10:
            nowaLista.append(liczba)


    nowaLista.sort(reverse=True)
    wynik = str(nowaLista) + ", łącznie {} elementów.".format(len(nowaLista))
    return print(wynik)

mniejszeOd10String(lista)

#WERSJA DLA ZAAWANSOWANYCH
print([liczba for liczba in lista if liczba < 10])