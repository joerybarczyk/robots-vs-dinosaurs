from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power_level = 100
        self.weapon = None
        self.available_weapons = [Weapon("Glock 19", 35), Weapon("Buzz Saw", 40), Weapon("Stun Gun", 30)]
    
    # Reduce opponents health by robot's weapon attack power, deplete robot power level and print result
    def attack(self, dinosaur):
        self.power_level -= 10

        dinosaur.health -= self.weapon.attack_power
        if (dinosaur.health < 0):
            dinosaur.health = 0
            dinosaur.energy = 0

        print(f"  {self.name} attacks {dinosaur.name} with a {self.weapon.name} for {self.weapon.attack_power} damage!")
        print(f"  {dinosaur.name} health remaining: ({dinosaur.health}/100)\n")
        if (dinosaur.health == 0):
            print(f"  {dinosaur.name} has died!\n")

    # Prompt user to select from weapons list, and set choice as robot's weapon
    def choose_weapon(self):
        while(True):
            print(f"\nPlease select a weapon for {self.name} (number):")
            self.print_weapons_list()
            weapon_choice = input(">>> ")
            if weapon_choice.isnumeric() and int(weapon_choice) in range(len(self.available_weapons)):
                self.weapon = self.available_weapons[int(weapon_choice)]
                break
            else:
                print("ERROR: Please enter the number of the weapon you want to select.")

    # Print a list of weapon choices for robot
    def print_weapons_list(self):
        for i in range(len(self.available_weapons)):
            print(f"({i})\t{self.available_weapons[i].name}\tDamage: {self.available_weapons[i].attack_power}")
