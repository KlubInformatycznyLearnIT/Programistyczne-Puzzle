def stoLat():
    wiek = int(input("Podaj swój wiek: "))
    rokKiedy100Lat = (2018-wiek)+100
    kiedy100Lat = rokKiedy100Lat-2018
    print("Lat potrzebnych do osiągnięcia wieku 100 lat: {}".format(kiedy100Lat))
    print("Rok osiągnięcia wieku 100 lat: {}".format(rokKiedy100Lat))

stoLat()

def stoLatUzytkownika():
    wiek = int(input("Podaj swój wiek: "))
    pozadanyWiek = int(input("Ile chcesz mieć lat?: "))
    rokKiedyPozadanyWiek = (2018 - wiek) + pozadanyWiek
    kiedyPozadanyWiek = rokKiedyPozadanyWiek - 2018
    print("Lat potrzebnych do osiągnięcia wieku {} lat: {}".format(pozadanyWiek, kiedyPozadanyWiek))
    print("Rok osiągnięcia wieku 100 lat: {}".format(rokKiedyPozadanyWiek))

stoLatUzytkownika()