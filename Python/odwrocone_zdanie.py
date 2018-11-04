# metoda nr1
def odwrocZdanie1(x):
    y = x.split()
    result = []
    for word in y:
        result.insert(0, word)
    return " ".join(result)


# metoda nr2
def odwrocZdanie2(x):
    y = x.split()
    return " ".join(y[::-1])


# metoda nr3
def odwrocZdanie3(x):
    y = x.split()
    return " ".join(reversed(y))


# metoda nr4
def odwrocZdanie4(x):
    y = x.split()
    y.reverse()
    return " ".join(y)


# test code
test1 = input("Wpisz zdanie: ")
print(odwrocZdanie1(test1))
print(odwrocZdanie2(test1))
print(odwrocZdanie3(test1))
print(odwrocZdanie4(test1))