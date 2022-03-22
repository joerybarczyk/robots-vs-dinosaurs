from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    # Add dinosaurs to herd
    def create_herd(self):
        self.dinosaurs.append(Dinosaur("Velociraptor", 50))
        self.dinosaurs.append(Dinosaur("Tyranosaurus", 25))
        self.dinosaurs.append(Dinosaur("Baby Chicken", 5))

    # Returns True if every dino in the herd is at 0 health
    def is_dead(self):
        dead_dinos = 0
        for dino in self.dinosaurs:
            if dino.health == 0:
                dead_dinos += 1
        
        if dead_dinos == len(self.dinosaurs):
            return True

        return False

    # Print dinosaurs and their statuses
    def show_herd(self):
        for i in range(len(self.dinosaurs)):
            status = f"  {self.dinosaurs[i].name}"
            if self.dinosaurs[i].health == 0:
                status += "\tDEAD"
            else:
                status += f"\tHealth: {self.dinosaurs[i].health}/100\tEnergy: {self.dinosaurs[i].energy}/100"
            print(status)
        print('\n')