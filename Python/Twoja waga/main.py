mojaWaga = 90
mojaWagaNaKsiezycu = mojaWaga * 0.165
for x in range(1,16):
    print("Moja waga na Ziemii:{0}kg, moja Waga na ksiezycu:{1} -- rok {2}".format(mojaWaga, mojaWagaNaKsiezycu, x))
    mojaWaga += 2
    mojaWagaNaKsiezycu = mojaWaga * 0.165
