# Car class
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        
    def __str__(self):
        """Converts the object into a string."""
        return f"Make: {self.make}\nModel: {self.model}\nColor: {self.color}\nMileage: {self.mileage}"