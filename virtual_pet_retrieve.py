from tkinter import *

OVERWEIGHT = 200
MIN_UNITS = 1
MAX_UNITS = 200


class Pet:
    def __init__(self, name=None, weight=0):
        self.name = name.title()
        self.weight = weight

    def feed(self, units):
        if self.weight > 0:
            self.weight += units
        return self.weight

    def exercise(self, units):
        if self.weight > 0:
            self.weight -= units
        return self.weight

    def __str__(self):
        if self.weight <= 0:
            return f"RIP {self.name}"
        elif self.weight > OVERWEIGHT:
            return f"{self.name} :-("
        else:
            return f"{self.name} now weighs {self.weight}"

class PetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Pet")
        self.pet = None

        self.label = Label(root, text= "Name")
        self.label.grid(row= 0, column= 0)

        self.entry = (root)
        self.entry.grid(row= 0, column= 1)

        self.button = Button(root, text= "Submit")
        self.button.grid(row= 1, column= 0, columnspan= 2)