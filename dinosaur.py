class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
        self.energy = 100
    
    # Reduce opponents health by dinosaur's attack power, reduce dinosaur energy and print result
    def attack(self, robot):
        self.energy -= 10
        robot.health -= self.attack_power

        if (robot.health < 0):
            robot.health = 0
            robot.power_level = 0
            
        print(f"  {self.name} attacks {robot.name} for {self.attack_power} damage!")
        print(f"  {robot.name} health remaining: ({robot.health}/100)\n")
        if (robot.health == 0):
            print(f"  {robot.name} has been destroyed!\n")