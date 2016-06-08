from car import *
from monster import *

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
    
