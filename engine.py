from time import sleep
from car import *

car_type = input("What car do you want? Available cars are: pilot and versa note ")
if car_type == "pilot":
    car = Car("honda", "pilot", 2003, 19, "blue")
    car.specs()
    car.drive()
elif car_type == "versa":
    car = Car("nissan", "versa note", 2015, 10, "silver")
    car.specs()
    car.drive()
else:
    print("what?")

while car.at_fight == True:
    car.fight_car()
    print("You've been hit, your health is:", car.health)
    sleep(random.randint(1, 5))
    car.get_user_input()
