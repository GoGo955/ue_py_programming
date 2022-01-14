class Klient:

    def __init__(
        self,
        id: str,
        imie: str,
        nazwisko: str,
        zamowienie: list,
        lokalizacja: str
    ):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.zamowienie = zamowienie
        self.lokalizacja = lokalizacja

    def __str__(self):
        return f'{self.imie} {self.nazwisko}, z {self.lokalizacja} (id {self.id}), zlozyl zamowienie na {self.zamowienie[0].nazwa} oraz {self.zamowienie[1].nazwa}.'

    @property
    def get_id(self):
        return self.id

    @property
    def get_imie(self):
        return self.imie

    @property
    def get_nazwisko(self):
        return self.nazwisko

    @property
    def get_zamowienie(self):
        return self.zamowienie

    @property
    def get_lokalizacja(self):
        return self.lokalizacja
