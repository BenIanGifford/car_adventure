import random

class Monster():

    """The monster class"""

    def __init__(self, name):
        self.name = name
        self.health = random.randint(1, 25)
        self.damage = random.randint(1, 15)

    def fight(self):
        self.health = self.health - random.randint(1, 7)
