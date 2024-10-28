class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'Property at {self.address}, Area: {self.area} sqm, Rooms: {self.rooms}, Price: ${self.price}'

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'House at {self.address}, Area: {self.area} sqm, Rooms: {self.rooms}, Price: ${self.price}, Plot size: {self.plot} sqm'

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Flat at {self.address}, Area: {self.area} sqm, Rooms: {self.rooms}, Price: ${self.price}, Floor: {self.floor}'

house = House(200, 5, 500000, "123 Main St", 400)
flat = Flat(85, 3, 300000, "456 Second St", 4)

print(house)
print(flat)
