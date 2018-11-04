import random

def porownajLiczby(wylosowana, podana):
    krowyByki = [0,0]
    for i in range(len(wylosowana)):
        if wylosowana[i] == podana[i]:
            krowyByki[1] += 1
        else:
            krowyByki[0] += 1
    return krowyByki


gra = True
los = str(random.randint(1000, 9999))
proby = 0
print(los)
while gra:
    strzal_uzytkownika = input("Podaj 4-cyfrową liczbę lub wpisz \"exit\" by wyjść: ")
    if strzal_uzytkownika == "exit":
        break
    if int(strzal_uzytkownika) < 1000 or int(strzal_uzytkownika) > 9999:
        print("podaj 4-cyfrową liczbę!")
    else:
        iloscKrowyByki = porownajLiczby(los, strzal_uzytkownika)
        proby += 1
        print("Ilość krów: {}, ilość byków: {}".format(iloscKrowyByki[0], iloscKrowyByki[1]))

        if iloscKrowyByki[1] == 4:
            gra = False
            print("Wygrałeś! Trafiłeś poprawną liczbę ({}) po {} próbach.".format(los, proby))
            break
        #else:
            #print("Spróbuj jeszcze raz.")