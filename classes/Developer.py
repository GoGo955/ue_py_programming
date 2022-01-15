from classes.Mieszkanie import Mieszkanie
from classes.Dom import Dom

class Developer:


    def __init__(
        self,
        nazwa: str,
        dane_kontaktowe: str,
        mieszkanie: Mieszkanie,
        dom: Dom
    ) -> None:
        self.nazwa = nazwa
        self.dane_kontaktowe = dane_kontaktowe
        self.mieszkanie = mieszkanie
        self.dom = dom
    

    def __str__(self) -> str:
        pass


    @property
    def get_nazwa(self):
        return self.nazwa

    @property
    def get_dane_kontaktowe(self):
        return self.dane_kontaktowe

    @property
    def get_mieszkanie(self):
        return self.mieszkanie

    @property
    def get_dom(self):
        return self.dom