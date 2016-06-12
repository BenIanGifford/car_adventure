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

while 1 > 2:
    car.fight_car()
    print("You've been hit, your health is:", car.health)
    car.get_user_input()
    sleep(random.randint(1, 5))
    
if car.health <= 0:
    print("Your health is less than zero you are dead")
    exit()
