from classes.magazyn import Magazyn


class Produkt:

    def __init__(
            self, id: str,
            nazwa: str,
            cena: float,
            opis: str,
            magazyn: Magazyn
    ):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena
        self.opis = opis
        self.magazyn = magazyn

    def __str__(self):
        return f"Produkt {self.nazwa} z id {self.id} kosztuje {self.cena}. Jego opis to: {self.opis}. Znajduje się w {self.magazyn}"

    @property
    def get_id(self):
        return self.id

    @property
    def get_nazwa(self):
        return self.nazwa

    @property
    def get_cena(self):
        return self.cena

    @property
    def get_opis(self):
        return self.opis

    @property
    def get_magazyn(self):
        return self.magazyn
