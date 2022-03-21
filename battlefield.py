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

    def display_welcome(self):
        print('\n############################################################\nWELCOME TO ULTIMATE ROBOTS VS DINOSAURS SUPER SMACKDOWN 2022\n############################################################')

    def battle(self):
        while(True):
            self.team_dino_turn()
            if self.fleet.is_dead():
                print("\nDINOSAURS WIN!!!")
                break
            self.team_robo_turn()
            if self.herd.is_dead():
                print("\nROBOTS WIN!!!")
                break

    def team_dino_turn(self):
        print("\nDINOSAURS ATTACK THE ROBOTS!")
        self.show_dino_opponent_options()
        for dinosaur in self.herd.dinosaurs:
            if dinosaur.health != 0:
                self.dino_turn(dinosaur)

    def team_robo_turn(self):
        print("\nROBOTS ATTACK THE DINOSAURS!")
        self.show_robo_opponent_options()
        for robot in self.fleet.robots:
            if robot.health != 0:
                self.robo_turn(robot)

    def dino_turn(self, dinosaur):
        robo_target = random.choice(self.fleet.robots)
        if robo_target.health == 0:
            robo_target = random.choice(self.fleet.robots)
        dinosaur.attack(robo_target)
        
    def robo_turn(self, robot):
        dino_target = random.choice(self.herd.dinosaurs)
        if dino_target.health == 0:
            dino_target = random.choice(self.herd.dinosaurs)
        robot.attack(dino_target)

    def show_dino_opponent_options(self):
        for i in range(len(self.herd.dinosaurs)):
            print(f"  {self.herd.dinosaurs[i].name}\tHealth: {self.herd.dinosaurs[i].health}/100")
        print('\n')

    def show_robo_opponent_options(self):
        for i in range(len(self.fleet.robots)):
            print(f"  {self.fleet.robots[i].name}\tHealth: {self.fleet.robots[i].health}/100")
        print('\n')
    
    def display_winners(self):
        pass