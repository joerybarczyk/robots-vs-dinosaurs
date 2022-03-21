from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
        self.choose_robot_weapons()

    def create_fleet(self):
        self.robots.append(Robot("Itchy Bot"))
        self.robots.append(Robot("Scratchy Bot"))
        self.robots.append(Robot("Poochie Bot"))

    def choose_robot_weapons(self):
        print('\n#####################\nROBOTS SELECT WEAPONS\n#####################')
        for robot in self.robots:
            robot.choose_weapon()

    def is_dead(self):
        # Returns True if every robot in the fleet is at 0 health
        dead_robots = 0
        for robot in self.robots:
            if robot.health == 0:
                dead_robots += 1
        
        if dead_robots == len(self.robots):
            return True

        return False