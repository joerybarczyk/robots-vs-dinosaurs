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
        print('############################################################\nWELCOME TO ULTIMATE ROBOTS VS DINOSAURS SUPER SMACKDOWN 2022\n############################################################')

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass
        
    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        for i in range(len(self.herd.dinosaurs)):
            print(f"({i})\t{self.herd.dinosaurs[i].name}\tHealth: {self.herd.dinosaurs[i].health}/100")

    def show_robo_opponent_options(self):
        for i in range(len(self.fleet.robots)):
            print(f"({i})\t{self.fleet.robots[i].name}\tHealth: {self.fleet.robots[i].health}/100")
    
    def display_winners(self):
        pass

battlefield = Battlefield()
battlefield.run_game()