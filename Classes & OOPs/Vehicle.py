"""Code to explain details around Python classes and it's methods"""


class Vehicle:
    def __init__(self, brand, model, transmission):
        self.brand = brand
        self.model = model
        self.transmission = transmission
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print('Gas tank is now full.')

    def drive(self):
        print(f'The {self.model} is now driving.')


vehicle_object = Vehicle("Honda", "Sedan", "Auto")
print(vehicle_object.brand, vehicle_object.model, vehicle_object.transmission)

# Calling methods
vehicle_object.fuel_up()
vehicle_object.drive()
