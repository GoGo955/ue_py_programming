class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: str
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"library, which located in {self.city} (zip code - {self.zip_code}), "
            f"at {self.street}.Library is open {self.open_hours}, "
            f"and the contact number is {self.phone}"
        )
