import datetime

def stoLatUzytkownika():
    wiek = int(input("Podaj swój wiek: "))
    pozadanyWiek = int(input("Ile chcesz mieć lat?: "))
    dzis = datetime.datetime.now()
    rokKiedyPozadanyWiek = (dzis.year - wiek) + pozadanyWiek
    kiedyPozadanyWiek = rokKiedyPozadanyWiek - dzis.year
    print("Lat potrzebnych do osiągnięcia wieku {} lat: {}".format(pozadanyWiek, kiedyPozadanyWiek))
    print("Rok osiągnięcia wieku 100 lat: {}".format(rokKiedyPozadanyWiek))

stoLatUzytkownika()