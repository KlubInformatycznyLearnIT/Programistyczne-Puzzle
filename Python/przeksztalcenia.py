lista = [31246,3421,3,4620,321,238,1235,235236,213,346,2,23,2347,317,1344,317]

parzyste = [parzysta for parzysta in lista if parzysta % 2 == 0]
nieparzyste = [nieparzysta for nieparzysta in lista if nieparzysta % 2 != 0]

print("Parzyste: {}".format(parzyste))
print("Nieparzyste: {}".format(nieparzyste))