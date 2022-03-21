from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        self.robots.append(Robot("Itchy Bot"))
        self.robots.append(Robot("Scratchy Bot"))
        self.robots.append(Robot("Poochie Bot"))