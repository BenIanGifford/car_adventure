"""Car module for the hit text based adventure
Car Adventure"""

import random

EVENTS = [
    "gas_station",
    "bank",
    "nothing",
    "nothing",
    "nothing",
    "nothing"]
BOOL = [
    True,
    False]
random.shuffle(EVENTS)
user_command = input("Ignore")

class Car():
    """Your car."""

    def __init__(self, make, model, year, fuel_capacity, color = None):
        """Atributtes of your car, fuel in gallons."""
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        self.money = 100
        self.fuel_capacity = fuel_capacity
        self.fuel_level = self.fuel_capacity
        self.at_gas_station = False
        self.at_bank = False
        self.looted = False
        self.times_driven = 0
        self.banks_looted = 0
        self.times_refueled = 0
        if self.year < 2000:
            print("Your car is old")


    def refuel(self):
        """Fill up your gas."""
        self.times_refueled = self.times_refueled + 1

        if self.fuel_level >= self.fuel_capacity:
            print("Your tank is already full :P")
        elif self.fuel_level < self.fuel_capacity and self.at_gas_station == False:
            print("You are not at a gas station and therfore can't fill up")
        elif self.fuel_level < self.fuel_capacity and self.at_gas_station == True:
            for i in range(self.fuel_level, self.fuel_capacity):
                self.money = self.money -2
            print("Your fuel tank has been filled you have ", self.money, "Carmids left")
            self.fuel_level = self.fuel_capacity

        user_command = input("What do you want to do? ")

        if user_command == "refuel":
            car.refuel()
        elif user_command == "drive":
            car.drive()
        elif user_command == "specs":
            car.specs()
        elif user_command == "loot":
            car.loot()

    def drive(self):
        """Drive your car"""
        self.fuel_level = self.fuel_level -1
        self.times_driven = self.times_driven + 1

        if self.fuel_level > 1:
            print("Your car is moving")

        if self.fuel_level <= self.fuel_capacity /2 and self.fuel_level > 0:
            print(self.fuel_level -1)

        if self.fuel_level <= 1:
            print("You need more gas")
        elif random.choice(EVENTS) == "gas_station":
            self.at_gas_station = True
            print("You are at a gas station")
        elif random.choice(EVENTS) == "bank":
            self.at_bank = True
            self.looted = False
            print("You are at a bank")
        elif random.choice(EVENTS) != "gas_station":
            self.at_gas_station = False
        elif random.choice(EVENTS) != "bank":
            self.at_bank = False

        user_command = input("What do you want to do? ")

        if user_command == "refuel":
            car.refuel()
        elif user_command == "drive":
            car.drive()
        elif user_command == "specs":
            car.specs()
        elif user_command == "loot":
            car.loot()

        if self.fuel_level <= 0 and self.at_gas_station == False:
            print("Game over, you collected", self.money, "Carmids drove",
            self.times_driven, "times refueled", self.times_refueled,
            "and looted", self.banks_looted, "banks")

    def specs(self):
        """Display specs of your car"""
        print(self.color, self.year, self.make, self.model,
         self.fuel_capacity, "Gallons", self.money, "Carmids")
        user_command = input("What do you want to do? ")
        if user_command == "refuel":
           car.refuel()
        elif user_command == "drive":
            car.drive()
        elif user_command == "specs":
            car.specs()
        elif user_command == "loot":
            car.loot()

    def loot(self):
        """Loot any bank you are at"""
        self.banks_looted = self.banks_looted + 1
        if self.at_bank == True:
            if self.looted == True:
                print("No more money here")
            elif random.choice(BOOL) == False and self.at_bank == True:
                print("No money here")
            elif self.at_bank == True and self.looted == False:
                self.money = self.money + random.randrange(1,50)
                print("You found some money, you now have", self.money, "Carmids")

        if self.at_bank != True:
            self.at_bank = False
            print("you are not at a bank and therefore there is nothing to loot")
        self.looted = True

        user_command = input("What do you want to do? ")

        if user_command == "refuel":
            car.refuel()
        elif user_command == "drive":
            car.drive()
        elif user_command == "specs":
            car.specs()
        elif user_command == "loot":
            car.loot()

car_type = input("What car do you want? Available cars are: pilot ")
if car_type == "pilot":
    car = Car("honda", "pilot", 2003, 19, "blue")
    car.drive()
else:
    print("what?")
