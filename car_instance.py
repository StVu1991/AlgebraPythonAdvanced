class Car:
    def __init__(self, manufacturer, model, price):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price


hgss_v1 = Car("Nissan", "Pajero", 1.00)
print(hgss_v1.manufacturer)
hgss_v2 = Car("Land Rover", "Discovery", 1.00)
print(hgss_v2.manufacturer)