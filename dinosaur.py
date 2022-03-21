class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
    
    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{self.name} attacks {robot.name}!")
        print(f"{robot.name} health remaining: ({robot.health}/100)")