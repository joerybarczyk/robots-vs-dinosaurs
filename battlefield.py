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
        self.herd.show_herd()
        for dinosaur in self.herd.dinosaurs:
            if dinosaur.health != 0 and dinosaur.energy > 0:
                self.dino_turn(dinosaur)

    # Run turn for robot team
    def fleet_turn(self):
        print("\nROBOTS ATTACK THE DINOSAURS!")
        self.fleet.show_fleet()
        for robot in self.fleet.robots:
            if robot.health != 0 and robot.power_level > 0:
                self.robot_turn(robot)

    # Choose a random not-dead robot to attack 
    def dino_turn(self, dinosaur):
        dinosaur.attack(self.random_robot())
        
    # Choose a random not-dead dinosaur to attack
    def robot_turn(self, robot):
        robot.attack(self.random_dinosaur())

    # Choose a random robot that is still alive
    def random_robot(self):
        target = random.choice(self.fleet.robots)
        if target.health == 0:
            target = random.choice(self.fleet.robots)
        return target

    # Choose a random dinosaur that is still alive
    def random_dinosaur(self):
        target = random.choice(self.herd.dinosaurs)
        if target.health == 0:
            target = random.choice(self.herd.dinosaurs)
        return target