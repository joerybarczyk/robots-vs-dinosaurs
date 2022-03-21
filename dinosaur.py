class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
    
    def attack(self, robot):
        robot.health -= self.attack_power
        if (robot.health < 0):
            robot.health = 0
        print(f"  {self.name} attacks {robot.name}!")
        print(f"  {robot.name} health remaining: ({robot.health}/100)\n")
        if (robot.health == 0):
            print(f"  {robot.name} has been destroyed!\n")