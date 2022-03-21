from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Glock 19", 35)
    
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"{self.name} attacks {dinosaur.name} with a {self.weapon.name}!")
        print(f"{dinosaur.name} health remaining: ({dinosaur.health}/100)")
