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