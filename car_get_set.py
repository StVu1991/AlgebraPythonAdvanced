class Car:
    def __init__(self, manufacturer, model, price):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__price = price

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        self.__price = price

    def get_manufacturer(self):
        return self.__manufacturer

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    manufacturer = property (get_manufacturer, set_manufacturer)
    model = property(get_model, set_model)
    price = property(get_price, set_price)

car1 = Car("Nissan", "Pajero", 1.00)
print(car1.model)

car1.model = "Path Finder"
print(car1.model)
