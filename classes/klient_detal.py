from classes.klient import Klient


class KlientDetaliczny(Klient):

    def __init__(
        self,
        id: str,
        imie: str,
        nazwisko: str,
        zamowienie: list,
        lokalizacja: str,
        typ_klienta: str
    ):
        super().__init__(id, imie, nazwisko, zamowienie, lokalizacja)
        self.typ_klienta = typ_klienta

    def __str__(self):
        return f'Klient {self.imie} {self.nazwisko}, z {self.lokalizacja} (id {self.id}), zlozyl zamowienie na {self.zamowienie}. Typ klienta detalicznego to {self.typ_klienta}.'

    @property
    def get_typ_klienta(self):
        return self.typ_klienta
