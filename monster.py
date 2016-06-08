import random
class Monster():
    self.health = 50
    
    def fight(self):
        self.health = self.health - random.randint(1, 15)
    
        
