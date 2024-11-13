import module
import module as kitchen
from module import make_pizza as mp
import module as car_factory

module.make_pizza("pepperoni")
kitchen.make_pizza("mushrooms", "green peppers", "extra cheese")
mp("mushrooms", "green peppers", "extra cheese")

car_factory.reveal_car_specs(make="subaru", model="outback", color="blue")
car_factory.reveal_car_specs(make="toyota", model="tacoma", color="white")