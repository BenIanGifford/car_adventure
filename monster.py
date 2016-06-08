import random

class Monster():
  """The monster class"""
  def __init__(self):
        self.health = random.randint(1, 25)
        self.damage = random.randint(1, 15)
