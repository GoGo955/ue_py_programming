class Property:
    def __init__(self, area: int, rooms: int, price: int, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"This {self.area} m2, with {self.rooms} rooms property is at {self.address} " \
               f"and it's for {self.price}$."


class House(Property):
    def __init__(self, area: int, rooms: int, price: int, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return super().__str__() + f" It has a plot of {self.plot} m2."


class Flat(Property):
    def __init__(self, area: int, rooms: int, price: int, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return super().__str__() + f" It is at {self.floor} floors."


if __name__ == "__main__":
    house = House(120, 6, 1240000, "super street", 1000)
    flat = Flat(80, 4, 250000, "north streer", 6)

    print(house)
    print(flat)
