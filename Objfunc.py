class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    def honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
# Above is how you enter a funtion within a class
