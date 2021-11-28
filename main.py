class Magazyn:

    def __init__(self, id: str, nazwa: str, miasto: str, adres: str, pojemnosc: int):
        self._id = id
        self._nazwa = nazwa
        self._miasto = miasto
        self._adres = adres
        self._pojemnosc = pojemnosc

    def __str__(self):
        return f'{self.nazwa} z id {self.id}  w {self.miasto}, ' \
               f'przy ulicy {self.adres} (pojemnosc {self.pojemnosc} paczek)'

    @property
    def id(self):
        return self._id

    @property
    def nazwa(self):
        return self._nazwa

    @property
    def adres(self):
        return self._adres

    @property
    def pojemnosc(self):
        return self._pojemnosc

    @property
    def miasto(self):
        return self._miasto


class Produkt:

    def __init__(self, id: str, nazwa: str, cena: float, opis: str, komentarz: str):
        self._id = id
        self._nazwa = nazwa
        self._cena = cena
        self._opis = opis
        self._komentarz = komentarz

    def __str__(self):
        return f'{self.nazwa} z id {self.id} kosztuje {self.cena}. Jego opis to: {self.opis}. (komemtarz: {self.komentarz})'

    @property
    def id(self):
        return self._id

    @property
    def nazwa(self):
        return self._nazwa

    @property
    def cena(self):
        return self._cena

    @property
    def opis(self):
        return self._opis

    @property
    def komentarz(self):
        return self._komentarz


class Klient:

    def __init__(self, id: str, imie: str, nazwisko: str, zamowienie: list, lokalizacja: str):
        self._id = id
        self._imie = imie
        self._nazwisko = nazwisko
        self._zamowienie = zamowienie
        self._lokalizacja = lokalizacja

    def __str__(self):
        return f'{self.imie} {self.nazwisko}, z {self.lokalizacja} (id {self.id}), ' \
               f'zlozyl zamowienie na {zamowienie[0].nazwa} oraz {zamowienie[1].nazwa}.'

    @property
    def id(self):
        return self._id

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def zamowienie(self):
        return self._zamowienie

    @property
    def lokalizacja(self):
        return self._lokalizacja


class KlientDetaliczny(Klient):

    def __init__(self, id: str, imie: str, nazwisko: str, zamowienie: list, lokalizacja: str, typ_klienta: str):
        super().__init__(id, imie, nazwisko, zamowienie, lokalizacja)
        self._typ_klienta = typ_klienta

    def __str__(self):
        return f'Klient {self.imie} {self.nazwisko}, z {self.lokalizacja} (id {self.id}), ' \
               f'zlozyl zamowienie na {self.zamowienie}. Typ klienta detalicznego to {self.typ_klienta}.'

    @property
    def id(self):
        return self._id

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def zamowienie(self):
        return self._zamowienie

    @property
    def lokalizacja(self):
        return self._lokalizacja

    @property
    def typ_klienta(self):
        return self._typ_klienta


class KlientBiznesowy(Klient):

    def __init__(self, id: str, imie: str, nazwisko: str, zamowienie: list, lokalizacja: str, typ_biznesu: str):
        super().__init__(id, imie, nazwisko, zamowienie, lokalizacja)
        self._typ_biznesu = typ_biznesu

    def __str__(self):
        return f'Klient {self.imie} {self.nazwisko}, z {self.lokalizacja} (id {self.id}), ' \
               f'zlozyl zamowienie na {self.zamowienie}. Typ biznesu klienta to {self.typ_biznesu}.'

    @property
    def id(self):
        return self._id

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def zamowienie(self):
        return self._zamowienie

    @property
    def lokalizacja(self):
        return self._lokalizacja

    @property
    def typ_biznesu(self):
        return self._typ_biznesu()


class Zamowienie:

    def __init__(self, id: str, produkt: Produkt, klient: Klient, magazyn: Magazyn, kwota: int):
        self.id = id
        self.produkt = produkt
        self.klient = klient
        self.magazyn = magazyn
        self.kwota = kwota

    def __str__(self):
        return f'Zamowienie z id {self.id} zawiera {self.produkt}. Zlokalizowany w {self.magazyn}.' \
               f'Zamowil je {self.klient} (id {self.id}), i ma do zaplaty {self.kwota}'

    def wart_zam(self):
        return self.produkt.cena

    def adres_klienta(self):
        return f'Adres klienta to {self.klient.lokalizacja}.'

    @property
    def id(self):
        return self._id

    @property
    def produkt(self):
        return self._produkt

    @property
    def klient(self):
        return self._klient

    @property
    def magazyn(self):
        return self._magazyn

    @property
    def lokalizacja(self):
        return self._lokalizacja

    @property
    def kwota(self):
        return self._kwota

    @id.setter
    def id(self, value):
        self._id = value

    @produkt.setter
    def produkt(self, value):
        self._produkt = value

    @klient.setter
    def klient(self, value):
        self._klient = value

    @magazyn.setter
    def magazyn(self, value):
        self._magazyn = value

    @kwota.setter
    def kwota(self, value):
        self._kwota = value


if __name__ == "__main__":
    mag1 = Magazyn('id_mag_1', 'Magazyn pierwszy', 'Katowice', 'ul. adresowa 3/5', 100)
    prod1 = Produkt('id_ksiazki', 'Ksiazka1', 50, 'krotki opis1', 'dodatkowy komentarz1')
    prod2 = Produkt('id_ksiazki2', 'Ksiazka2', 66, 'krotki opis2', 'dodatkowy komentarz2')
    klient_det = KlientDetaliczny('id_kli_det', "Marek", 'Kondrat', [prod1, prod2], 'Katowice, ul. wyborowa 4/5', "typ_detal_1")
    zam1 = Zamowienie('id_zam_1', prod1, klient_det, mag1, 150)

    print(zam1)
    print(zam1.wart_zam())
    print(zam1.adres_klienta())
