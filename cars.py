__author__ = "Stjepan"


class Car:
    def __init__(self, make, model, price, inventory):
        self.__make = make
        self.__model = model
        self.__price = price
        self.__inventory = inventory

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_inventory(self):
        return self.__inventory

    def set_inventory(self, inventory):
        self.__inventory = inventory

    make = property(get_make, set_make)
    model = property(get_model, set_model)
    price = property(get_price, set_price)
    inventory = property(get_inventory, set_inventory)

    def display(self):
        print("jesam")
        print("{0} {1} - price: {2:.2f}, inventory: {3:d}".format(self.make, self.model, self.price, self.inventory))
        print("nisam")

    def sellCar(self, quantity):
        self.__inventory = self.__inventory - quantity

class Sedan(Car):
    def __init__ (self, make, model, price, inventory, doors, seats):
        super(Sedan, self).__init__(make, model, price, inventory)
        self.__doors__ = doors
        self.__seats__ = seats

    def get_doors(self):
        return self.__doors__

    def set_doors(self, doors):
        self.__doors__ = doors

    def get_seats(self):
        return self.__seats__

    def set_seats(self, seats):
        self.__seats__ = seats

    doors = property(get_doors, set_doors)
    seats = property(get_seats, set_seats)

    def display(self):
        print("baba")
        print("This sedan has {0} doors and {1} seats ". format(self.doors, self.seats))
