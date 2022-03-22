import random

from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()

    # Print welcome screen
    def display_welcome(self):
        print('\n############################################################\nWELCOME TO ULTIMATE ROBOTS VS DINOSAURS SUPER SMACKDOWN 2022\n############################################################')

    # Run main game loop
    def battle(self):
        while(True):
            self.herd_turn()
            if self.fleet.is_dead():
                print("\nDINOSAURS WIN!!!")
                break
            self.fleet_turn()
            if self.herd.is_dead():
                print("\nROBOTS WIN!!!")
                break

    # Run turn for dinosaur team
    def herd_turn(self):
        print("\nDINOSAURS ATTACK THE ROBOTS!")
        self.show_dino_opponent_options()
        for dinosaur in self.herd.dinosaurs:
            if dinosaur.health != 0 and dinosaur.energy > 0:
                self.dino_turn(dinosaur)

    # Run turn for robot team
    def fleet_turn(self):
        print("\nROBOTS ATTACK THE DINOSAURS!")
        self.show_robo_opponent_options()
        for robot in self.fleet.robots:
            if robot.health != 0 and robot.power_level > 0:
                self.robo_turn(robot)

    # Choose a random not-dead robot to attack 
    def dino_turn(self, dinosaur):
        robo_target = random.choice(self.fleet.robots)
        if robo_target.health == 0:
            robo_target = random.choice(self.fleet.robots)
        dinosaur.attack(robo_target)
        
    # Choose a random not-dead dinosaur to attack
    def robo_turn(self, robot):
        dino_target = random.choice(self.herd.dinosaurs)
        if dino_target.health == 0:
            dino_target = random.choice(self.herd.dinosaurs)
        robot.attack(dino_target)

    # Print dinosaurs in herd and their statuses
    def show_dino_opponent_options(self):
        for i in range(len(self.herd.dinosaurs)):
            status = f"  {self.herd.dinosaurs[i].name}"
            if self.herd.dinosaurs[i].health == 0:
                status += "\tDEAD"
            else:
                status += f"\tHealth: {self.herd.dinosaurs[i].health}/100\tEnergy: {self.herd.dinosaurs[i].energy}/100"
            print(status)
        print('\n')

    # Print robots in fleet and their statuses
    def show_robo_opponent_options(self):
        for i in range(len(self.fleet.robots)):
            status = f"  {self.fleet.robots[i].name}"
            if self.fleet.robots[i].health == 0:
                status += "\tDEAD"
            else:
                status += f"\tHealth: {self.fleet.robots[i].health}/100\tPower Level: {self.fleet.robots[i].power_level}/100"
            print(status)
        print('\n')
    
    def display_winners(self):
        pass