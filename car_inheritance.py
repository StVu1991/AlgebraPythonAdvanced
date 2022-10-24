class Car:
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model


class Sedan (Car):
    def __init__(self, manufacturer, model, doors, seats):
        super(Sedan, self).__init__(manufacturer, model)
        self.doors = doors
        self.seats = seats


sedan = Sedan("Renault", "Laguna", 4, 4)
print(sedan.doors)
print(sedan.seats)
print(sedan.manufacturer)