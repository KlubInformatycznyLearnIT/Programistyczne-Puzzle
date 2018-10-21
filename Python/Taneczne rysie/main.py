class Rysie:
    def lewaNogaPrzod(self):
        print('lewa noga w przód!')

    def lewaNogaTyl(self):
        print('lewa noga w tył!')

    def prawaNogaPrzod(self):
        print('prawa noga w przód!')

    def prawaNogaTyl(self):
        print('prawa noga w tył!')

    def obrot(self):
        print('i obróóót!')

    def taniec(self):
        self.lewaNogaPrzod()
        self.lewaNogaTyl()
        self.prawaNogaPrzod()
        self.prawaNogaTyl()
        self.lewaNogaTyl()
        self.obrot()


Eustachy = Rysie()
Eustachy.taniec()
