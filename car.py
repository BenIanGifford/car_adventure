"""Car module for the hit text based adventure
Car Adventure"""

import random

EVENTS = [
    "gas_station",
    "bank",
    "hospital",
    "nothing",
    "nothing",
    "nothing"]
BOOL = [
    True,
    False]
random.shuffle(EVENTS)
USER_COMMAND = input("Ignore")

class Car():
    """Your car."""

    def __init__(self, make, model, year, fuel_capacity, color = None):
        """Atributtes of your car, fuel in gallons."""
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        self.money = 100
        self.health = 50
        self.fuel_capacity = fuel_capacity
        self.fuel_level = self.fuel_capacity
        self.at_gas_station = False
        self.at_bank = False
        self.at_hospital = False
        self.looted = False
        self.times_driven = 0
        self.banks_looted = 0
        self.times_refueled = 0
        if self.year < 2000:
            print("Your car is old")

    def get_user_input(self):
        USER_COMMAND = input("What do you want to do? ")

        if USER_COMMAND == "refuel":
            car.refuel()
        elif USER_COMMAND == "drive":
            car.drive()
        elif USER_COMMAND == "specs":
            car.specs()
        elif USER_COMMAND == "loot":
            car.loot()
        elif USER_COMMAND == "heal":
            car.heal()

    def heal(self):
        self.health = self.health
        print("You've been healed! Your health is now:", self.health)
        self.get_user_input()


    def refuel(self):
        """Fill up your gas."""

        if self.fuel_level >= self.fuel_capacity:
            print("Your tank is already full :P")
        elif self.fuel_level < self.fuel_capacity and self.at_gas_station == False:
            print("You are not at a gas station and therfore can't fill up")
        elif self.fuel_level < self.fuel_capacity and self.at_gas_station == True:
            for i in range(self.fuel_level, self.fuel_capacity):
                self.money = self.money -2
            print("Your fuel tank has been filled you have ", self.money, "Carmids left")
            self.fuel_level = self.fuel_capacity
            self.times_refueled = self.times_refueled + 1

        self.get_user_input()


    def drive(self):
        """Drive your car"""

        if self.fuel_level > 0:
            print("Your car is moving")
            self.times_driven = self.times_driven + 1
            self.fuel_level = self.fuel_level -1

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
        elif random.choice(EVENTS) == "hospital":
            self.at_hospital = True
            print("You are at a hoapital")
        elif random.choice(EVENTS) != "gas_station":
            self.at_gas_station = False
        elif random.choice(EVENTS) != "bank":
            self.at_bank = False

        if self.fuel_level <= 0 and self.at_gas_station == False:
            print("Game over, you collected", self.money, "Carmids drove",
            self.times_driven, "times refueled", self.times_refueled,
            "and looted", self.banks_looted, "banks")

        self.get_user_input()


    def specs(self):
        """Display specs of your car"""
        print(self.color, self.year, self.make, self.model,
         self.fuel_capacity, "Gallons", self.money, "Carmids")
        self.get_user_input()

    def loot(self):
        """Loot any bank you are at"""
        if self.at_bank == True:
            if self.looted == True:
                print("No more money here")
            elif random.choice(BOOL) == False and self.at_bank == True:
                print("No money here")
                self.banks_looted = self.banks_looted + 1
            elif self.at_bank == True and self.looted == False:
                self.money = self.money + random.randrange(1, 50)
                print("You found some money, you now have", self.money, "Carmids")
                self.banks_looted = self.banks_looted + 1

        if self.at_bank != True:
            self.at_bank = False
            print("you are not at a bank and therefore there is nothing to loot")
        self.looted = True

        self.get_user_input()


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
