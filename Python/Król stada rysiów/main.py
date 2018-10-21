class Rysie:
    # Atrybuty klasy
    wlasciwosci = 'ssak'

    # Initializer / Instance Attributes
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek


#wywołaj obiekty Rysie
jasiek = Rysie("Jasiek", 7)
michal = Rysie("Michal", 4)
krzychu = Rysie("Krzychu", 5)


# Określ najstarszego rysia
def get_biggest_number(*args):  # *args - przyjmuje dowolną ilość parametrów
    return print("Najstarszy ryś ma {} lat.".format(max(args)))  # max(args) - wypisuje maksymalną wartość z podanych argumentów


get_biggest_number(jasiek.wiek, michal.wiek, krzychu.wiek)
