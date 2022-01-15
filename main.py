from classes.Developer import Developer
from classes.Dom import Dom
from classes.Mieszkanie import Mieszkanie
from classes.Zamowienie import Zamowienie


if __name__ == "__main__":
    m1 = Mieszkanie("Czerwona 5", 350000, 45, "ogrzewanie gazowe")
    d1 = Dom("Niebieska 3/4", 500000, 90, "ogrzewanie podlogowe", 140)
    dev = Developer("Dom-bud", "435 535 535", "dombud@dev.pl", m1, d1)
    zam = Zamowienie()
    zam.developer = dev
    zam.dom = zam.get_developer.get_dom
    zam.mieszkanie = zam.get_developer.get_mieszkanie
    print(zam, f"Kwota zamowienia to {zam.oblicz_kwote_zam()}, a laczny metraz to {zam.oblicz_metraz()}")

