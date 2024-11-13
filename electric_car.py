import car as base

class ElectricCar(base.Car):
    """
    Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40  

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def __str__(self):
        return "\n" + super().__str__() + f"\nBattery size: {self.battery_size}-kWh"