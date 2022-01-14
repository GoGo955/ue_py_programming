from classes.magazyn import Magazyn
from classes.klient import Klient
from classes.produkt import Produkt


class Zamowienie:

    def __init__(
        self,
        id: str,
        produkt: Produkt,
        klient: Klient,
        magazyn: Magazyn,
        kwota: int
    ):
        self.id = id
        self.produkt = produkt
        self.klient = klient
        self.magazyn = magazyn
        self.kwota = kwota

    def __str__(self):
        return f'Zamowienie z id {self.id} zawiera {self.produkt.get_nazwa}, zlokalizowany w {self.magazyn.get_nazwa}. Zamowil je {self.klient.get_imie} (id {self.id}), i ma do zaplaty {self.kwota}.'

    def wart_zam(self):
        return self.produkt.cena

    def adres_klienta(self):
        return f'Adres klienta to {self.klient.lokalizacja}.'

    @property
    def get_id(self):
        return self.id

    @property
    def get_produkt(self):
        return self.produkt

    @property
    def get_klient(self):
        return self.klient

    @property
    def get_magazyn(self):
        return self.magazyn

    @property
    def get_lokalizacja(self):
        return self.lokalizacja

    @property
    def get_kwota(self):
        return self.kwota

    @get_id.setter
    def get_id(self, value):
        self.id = value

    @get_produkt.setter
    def get_produkt(self, value):
        self.produkt = value

    @get_klient.setter
    def get_klient(self, value):
        self.klient = value

    @get_magazyn.setter
    def get_magazyn(self, value):
        self.magazyn = value

    @get_kwota.setter
    def get_kwota(self, value):
        self.kwota = value
