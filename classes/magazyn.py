class Magazyn:

    def __init__(
        self, id: str,
        nazwa: str,
        miasto: str,
        adres: str,
        pojemnosc: int
    ):
        self.id = id
        self.nazwa = nazwa
        self.miasto = miasto
        self.adres = adres
        self.pojemnosc = pojemnosc

    def __str__(self):
        return f'Magazyn {self.nazwa} z id {self.id}  w {self.miasto}, ' \
               f'przy ulicy {self.adres} o pojemnosci {self.pojemnosc}.'

    @property
    def get_id(self):
        return self.id

    @property
    def get_nazwa(self):
        return self.nazwa

    @property
    def get_adres(self):
        return self.adres

    @property
    def get_pojemnosc(self):
        return self.pojemnosc

    @property
    def get_miasto(self):
        return self.miasto
