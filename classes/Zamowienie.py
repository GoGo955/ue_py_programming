from classes.Developer import Developer


class Zamowienie:


    def __init__(self) -> None:
        self.developer = None
        self.mieszkanie = None
        self.dom = None
        self.kwota_zam = None


    def __str__(self) -> str:
        pass

    @property
    def get_developer(self):
        return self.developer

    @property
    def get_mieszkanie(self):
        return self.mieszkanie

    @property
    def get_dom(self):
        return self.dom

    @property
    def get_kwota_zam(self):
        return self.kwota_zam

    @get_developer.setter
    def set_developer(self, dev):
        self.developer = dev
