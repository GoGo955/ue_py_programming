from classes.klient import Klient


class KlientBiznesowy(Klient):

    def __init__(
        self,
        id: str,
        imie: str,
        nazwisko: str,
        zamowienie: list,
        lokalizacja: str,
        typ_biznesu: str
    ):
        super().__init__(id, imie, nazwisko, zamowienie, lokalizacja)
        self.typ_biznesu = typ_biznesu

    def __str__(self):
        return f'Klient {self.imie} {self.nazwisko}, z {self.lokalizacja} (id {self.id}), zlozyl zamowienie na {self.zamowienie}. Typ biznesu klienta to {self.typ_biznesu}.'

    @property
    def get_typ_biznesu(self):
        return self.typ_biznesu
