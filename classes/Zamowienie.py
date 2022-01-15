from multiprocessing.spawn import import_main_path
from classes.Developer import Developer
from classes.Mieszkanie import Mieszkanie
from classes.Dom import Dom

class Zamowienie:


    def __init__(self) -> None:
        self.developer = None
        self.dom = None
        self.mieszkanie = None


    def __str__(self) -> str:
        return f"Zamowienie sklada sie z {self.dom} oraz {self.mieszkanie}. Wlascicielem obiektow jest {self.developer.get_nazwa}."

    @property
    def get_developer(self):
        return self.developer

    @property
    def get_dom(self):
        return self.dom

    @property
    def get_mieszkanie(self):
        return self.mieszkanie


    @get_developer.setter
    def set_developer(self, dev: Developer):
        self.developer = dev

    @get_dom.setter
    def set_dom(self, dom: Dom):
        self.dom = dom

    @get_mieszkanie.setter
    def set_mieszkanie(self, mieszkanie: Mieszkanie):
        self.mieszkanie = mieszkanie


    def oblicz_kwote_zam(self):
        return round(self.mieszkanie.get_cena + self.dom.get_cena, 2)

    
    def oblicz_metraz(self):
        return self.mieszkanie.get_metraz + self.dom.get_metraz
