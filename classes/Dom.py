from classes.Mieszkanie import Mieszkanie


class Dom(Mieszkanie):

    def __init__(
            self,
            adres: str,
            cena: int,
            metraz: int,
            ogrzewanie: str,
            powierzchnia_ogrodu: int
        ) -> None:
        super().__init__(adres, cena, metraz, ogrzewanie)
        self.pow_ogr = powierzchnia_ogrodu


    def __str__(self) -> str:
        return f"Dom przy {self.get_adres}, o powierzchni {self.get_metraz} i ogrodzie {self.get_pow_ogr}m2 kosztuje {self.get_cena}. Typ ogrzewania to {self.get_ogrzewanie}"


    @property
    def get_pow_ogr(self):
        return self.pow_ogr
