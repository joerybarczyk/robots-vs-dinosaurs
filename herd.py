from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
    
    def create_herd(self):
        self.dinosaurs.append(Dinosaur("Velociraptor", 50))
        self.dinosaurs.append(Dinosaur("T. Rex", 25))
        self.dinosaurs.append(Dinosaur("Chicken", 5))