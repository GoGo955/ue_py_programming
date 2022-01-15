class Mieszkanie:

    def __init__(
        self,
        adres: str,
        cena: int,
        metraz: int,
        ogrzewanie: str
    ) -> None:
        self.adres = adres
        self.cena = cena
        self.metraz = metraz
        self.ogrzewanie = ogrzewanie
    

    def __str__(self) -> str:
        return f"Mieszkanie przy {self.get_adres}, o powierzchni {self.get_metraz} kosztuje {self.get_cena}. Typ ogrzewania to {self.ogrzewanie}"


    @property
    def get_adres(self):
        return self.adres

    @property
    def get_cena(self):
        return self.cena

    @property
    def get_metraz(self):
        return self.metraz

    @property
    def get_ogrzewanie(self):
        return self.ogrzewanie
