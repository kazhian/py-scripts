import car
import electric_car as ecar

# Using Car class
my_car = car.Car('audi', 'a4', 'blue')
print(my_car)

my_car.drive(10)
print(my_car)

# Using ElectricCar class
e_car = ecar.ElectricCar('tesla', 'model s', 'red')
print(e_car)
