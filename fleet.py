from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        self.robots.append(Robot("Itchy Bot"))
        self.robots.append(Robot("Scratchy Bot"))
        self.robots.append(Robot("Poochie Bot"))

    def is_dead(self):
        # Returns True if every robot in the fleet is at 0 health
        dead_robots = 0
        for robot in self.robots:
            if robot.health == 0:
                dead_robots += 1
        
        if dead_robots == len(self.robots):
            return True

        return False