from classes.Mieszkanie import Mieszkanie
from classes.Dom  import Dom


class Developer:

    def __init__(
        self,
        nazwa: str,
        telefon: str,
        email: str,
        mieszkanie: Mieszkanie,
        dom: Dom
    ) -> None:
        self.nazwa = nazwa
        self.telefon = telefon
        self.mieszkanie = mieszkanie
        self.email = email
        self.dom = dom 

    def __str__(self) -> str:
        return f"Developer {self.nazwa} o danych kontaktowych {self.telefon} {self.email} posiada {self.mieszkanie.get_adres} oraz {self.dom.get_adres}"

    @property
    def get_nazwa(self):
        return self.nazwa

    @property
    def get_telefone(self):
        return self.telefon

    @property
    def get_mieszkanie(self):
        return self.mieszkanie

    @property
    def get_dom(self):
        return self.dom

    @property
    def get_email(self):
        return self.email