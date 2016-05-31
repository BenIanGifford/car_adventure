import random

events = [
    "gas_station",
    "nothing",
    "nothing",
    "nothing",
    "nothing",
    "nothing"]
random.shuffle(events)

class car():
        """Your car."""

        def __init__(self, make, model, year, fuel_capacity, color=None):
            """Atributtes of your car, fuel in gallons."""
            self.color = color
            self.make = make
            self.model = model
            self.year = year
            self.fuel_capacity = fuel_capacity
            self.fuel_level = self.fuel_capacity
            if self.year < 2000:
                print("Your car is old")
            
        def refuel(self):
            """Fill up your gas."""
            at_gas_station = False
            
            if random.choice(events) == "gas_station":
                    at_gas_station = True
                    print("You are at a gas station")
            elif random.choice(events) != "gas_station":
                at_gas_station = False
                
            if self.fuel_level >= self.fuel_capacity:
                print("Your tank is already full :P")
            elif self.fuel_level < self.fuel_capacity and at_gas_station == False:
                print("You are not at a gas station and therfore can't fill up") 
            elif self.fuel_level < self.fuel_capacity and at_gas_station == True:
                self.fuel_level = self.fuel_capacity
                print("Your fuel tank is full") 

        def drive(self):
            """Drive your car"""
            self.fuel_level = self.fuel_level -1
            
            if self.fuel_level < 1:
                print("You need more gas")
            elif self.fuel_level <= self.fuel_capacity /2:
                print(self.fuel_level -1)
            else:
                print("The car is moving")

        def specs(self):
            """Display specs of your car"""
            print(self.color, self.year, self.make, self.model, self.fuel_capacity, "Gallons")
