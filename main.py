from classes import magazyn, produkt, klient_detal, zamowienie

if __name__ == "__main__":
    mag1 = magazyn.Magazyn('id_mag_1', 'Magazyn pierwszy', 'Katowice', 'ul. adresowa 3/5', 100)
    prod1 = produkt.Produkt('id_ksiazki', 'Ksiazka1', 50, 'krotki opis1', 'dodatkowy komentarz1')
    prod2 = produkt.Produkt('id_ksiazki2', 'Ksiazka2', 66, 'krotki opis2', 'dodatkowy komentarz2')
    klient_det = klient_detal.KlientDetaliczny('id_kli_det', "Marek", 'Kondrat', [prod1, prod2], 'Katowice, ul. wyborowa 4/5', "typ_detal_1")
    zam1 = zamowienie.Zamowienie('id_zam_1', prod1, klient_det, mag1, 150)

    print(zam1)
    print(zam1.wart_zam())
    print(zam1.adres_klienta())
