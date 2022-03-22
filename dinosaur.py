import random

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.attack_names = ("Tail Whip", "Power Bite", "Claw Swipe")
        self.health = 100
        self.energy = 100
    
    # Reduce opponents health by dinosaur's attack power, reduce dinosaur energy and print result
    def attack(self, robot):
        self.energy -= 10
        robot.health -= self.attack_power

        if (robot.health < 0):
            robot.health = 0
            robot.power_level = 0

        # attack_name = self.get_random_attack_name()
        attack_name = self.choose_attack_name(robot)

        print(f"\n  {self.name} attacks {robot.name} with {attack_name} for {self.attack_power} damage!")
        print(f"  {robot.name} health remaining: ({robot.health}/100)\n")
        if (robot.health == 0):
            print(f"  {robot.name} has been destroyed!\n")

    def get_random_attack_name(self):
        random_attack_name = random.choice(self.attack_names)
        return random_attack_name

    def choose_attack_name(self, target):
        while(True):
            print(f"\nPlease select an attack for {self.name} to use against {target.name} (number):")
            self.print_attack_names()
            attack_name_choice = input(">>> ")
            if attack_name_choice.isnumeric() and int(attack_name_choice) in range(len(self.attack_names)):
                return self.attack_names[int(attack_name_choice)]
            else:
                print("ERROR: Please enter the number of the attack you want to use.")

    def print_attack_names(self):
        for i in range(len(self.attack_names)):
            print(f"({i})\t{self.attack_names[i]}")
