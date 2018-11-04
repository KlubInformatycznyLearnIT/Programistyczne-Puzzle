lista = [3426,34562,4573,11,43,4235,453,454,431,453431,7,9789,24,755]

for liczba in lista:
    a = [x for x in range(2,liczba) if liczba % x == 0]
    if len(a) == 0:
        print("{} jest liczbą pierwszą".format(liczba))
#    else:
#        print("{} nie jest liczbą pierwszą".format(liczba))

