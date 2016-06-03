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

class Car():
    """Your car."""

    def __init__(self, make, model, year, fuel_capacity, color=None):
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
        if self.year < 2000:
            print("Your car is old")
            
    def refuel(self):
        """Fill up your gas."""
                
        if self.fuel_level >= self.fuel_capacity:
            print("Your tank is already full :P")
        elif self.fuel_level < self.fuel_capacity and self.at_gas_station == False:
            print("You are not at a gas station and therfore can't fill up") 
        elif self.fuel_level < self.fuel_capacity and self.at_gas_station == True:
            for i in range(self.fuel_level, self.fuel_capacity):
                self.money = self.money -2
            print("Your fuel tank has been filled, you now have", self.money, "Carmids")
            self.fuel_level = self.fuel_capacity

    def drive(self):
        """Drive your car"""
        self.fuel_level = self.fuel_level -1
        
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

    def specs(self):
        """Display specs of your car"""
        print(self.color, self.year, self.make, self.model,
        self.fuel_capacity, "Gallons", self.money, "Carmids")
        
def loot(self):
        if self.at_bank == True:
            if self.looted == True:
                print("No more money here")
            if random.choice(BOOL) == False and self.at_bank == True:
                print("No money here")
            elif self.at_bank == True and self.looted == False:
                self.money = self.money + random.randrange(1,50)
                print("You found some money you now have", self.money, "Carmids")
                
        if self.at_bank != True:
            self.at_bank = False
            print("you are not at a bank and therefore there is nothing to loot")
        self.looted = True
