from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        self.dinosaurs.append(Dinosaur("Velociraptor", 50))
        self.dinosaurs.append(Dinosaur("Tyranosaurus", 25))
        self.dinosaurs.append(Dinosaur("Baby Chicken", 5))