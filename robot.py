from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power_level = 100
        self.weapon = Weapon("Glock 19", 35)
    
    def attack(self, dinosaur):
        self.power_level -= 10
        dinosaur.health -= self.weapon.attack_power
        if (dinosaur.health < 0):
            dinosaur.health = 0
            dinosaur.energy = 0
        print(f"  {self.name} attacks {dinosaur.name} with a {self.weapon.name}!")
        print(f"  {dinosaur.name} health remaining: ({dinosaur.health}/100)\n")
        if (dinosaur.health == 0):
            print(f"  {dinosaur.name} has died!\n")

    def choose_weapon(self):
        while(True):
            weapons_list = [Weapon("Glock 19", 35), Weapon("Buzz Saw", 40), Weapon("Stun Gun", 30)]
            print(f"\nPlease select a weapon for {self.name} (number):")
            for i in range(len(weapons_list)):
                print(f"({i})\t{weapons_list[i].name}\tDamage: {weapons_list[i].attack_power}")
            weapon_choice = input(">>> ")
            if weapon_choice.isnumeric() and int(weapon_choice) in range(len(weapons_list)):
                self.weapon = weapons_list[int(weapon_choice)]
                break
            else:
                print("ERROR: Please enter the number of the weapon you want to select.")

