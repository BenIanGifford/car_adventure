"""Car module for the hit text based adventure Car Adventure"""

import random
from monster import Monster

EVENTS = [
    "gas_station",
    "bank",
    "hospital",
    "fight",
    "fight",
    "fight"]
BOOL = [
    True,
    False]
random.shuffle(EVENTS)
USER_COMMAND = input("""Welcome to Car Adventure the hit text based adventure
by Benjamin Ian Gifford. Type exit or quit to quit""")

evilthing = Monster("Bill")

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
        self.damage = random.randint(1,10)
        self.fuel_capacity = fuel_capacity
        self.fuel_level = self.fuel_capacity
        self.at_gas_station = False
        self.at_bank = False
        self.at_hospital = False
        self.at_fight = False
        self.looted = False
        self.times_driven = 0
        self.times_fought = 0
        self.banks_looted = 0
        self.times_refueled = 0
        if self.year < 2000:
            print("Your car is old")


    def get_user_input(self):
        USER_COMMAND = input("What do you want to do? ")

        if USER_COMMAND.lower() == "refuel":
            self.refuel()
        elif USER_COMMAND.lower() == "drive":
            self.drive()
        elif USER_COMMAND.lower() == "specs":
            self.specs()
        elif USER_COMMAND.lower() == "loot":
            self.loot()
        elif USER_COMMAND.lower() == "heal":
            self.heal()
        elif USER_COMMAND.lower() == "fight":
            self.fight_monster()
        elif USER_COMMAND.lower() == "exit" or "quit":
            exit
            quit
        else:
            USER_COMMAND = input("What do you want to do? ")

            if USER_COMMAND.lower() == "refuel":
                self.refuel()
            elif USER_COMMAND.lower() == "drive":
                self.drive()
            elif USER_COMMAND.lower() == "specs":
                self.specs()
            elif USER_COMMAND.lower() == "loot":
                self.loot()
            elif USER_COMMAND.lower() == "heal":
                self.heal()
            elif USER_COMMAND.lower() == "fight":
                self.fight_monster
            elif USER_COMMAND.lower() == "exit" or "quit":
                exit
                quit

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
            print("You are at a hospital")
        elif random.choice(EVENTS) == "fight":
            self.at_fight = True
            evilthing.alive = True
            print("You have found a monster!")
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


    def fight_monster(self):
        if self.at_fight == True and evilthing.alive == True:
            evilthing.health = evilthing.health - self.damage
            print("Monster health is: ", evilthing.health)

            if evilthing.health <= 0:
                evilthing.alive = False
                print("The monster is dead!")
                self.get_user_input()
        elif self.at_fight != True or evilthing.alive != True:
            print("No more monsters here")
        self.get_user_input()

        def fight_car(self):
            if self.at_fight == True and evilthing.alive == True:
                self.health = self.health - evilthing.damage
