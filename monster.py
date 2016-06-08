from car import *
import random
import time

class Monster():

    """The monster class"""

    def __init__(self, name):
        self.name = name
        self.health = random.randint(1, 25)
        self.damage = random.randint(1, 15)
        self.alive = True
        
    def get_user_input(self):
        USER_COMMAND = input("What do you want to do? ")

        if USER_COMMAND.lower() == "refuel":
            car.refuel()
        elif USER_COMMAND.lower() == "drive":
            car.drive()
        elif USER_COMMAND.lower() == "specs":
            car.specs()
        elif USER_COMMAND.lower() == "loot":
            car.loot()
        elif USER_COMMAND.lower() == "heal":
            car.heal()
        elif USER_COMMAND.lower() == "fight":
            self.defend()
        elif USER_COMMAND.lower() == "exit" or "quit":
            exit
            quit
        else:
            USER_COMMAND = input("What do you want to do? ")

            if USER_COMMAND.lower() == "refuel":
                car.refuel()
            elif USER_COMMAND.lower() == "drive":
                self.drive()
            elif USER_COMMAND.lower() == "specs":
                car.specs()
            elif USER_COMMAND.lower() == "loot":
                car.loot()
            elif USER_COMMAND.lower() == "heal":
                car.heal()
            elif USER_COMMAND.lower() == "fight":
                 self.defend()
            elif USER_COMMAND.lower() == "exit" or "quit":
                exit
                quit


    def defend(self):
        self.health = self.health - random.randint(1, 7)
        print(self.health)
        if self.health <= 0:
            self.alive = False
        self.get_user_input()


    def attack(self):
        if Car.at_fight == True and self.alive == True:
            time.sleep(random.randint(1, 5))
            Car.health = Car.health - self.damage
        self.get_user_input()
