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
        self.shared_font = font.Font(size=12)

        self.label1 = Label(root, text= "Pet Name")
        self.label1.grid(row= 0, column= 0, sticky="nsew")

        self.entry1 = Entry(root)
        self.entry1.grid(row= 0, column= 1, sticky="nsew")

        self.label2 = Label(root, text= "Starting Weight")
        self.label2.grid(row= 1, column= 0, sticky="nsew")

        self.entry2 = Entry(root)
        self.entry2.grid(row= 1, column= 1, sticky="nsew")

        self.button1 = Button(root, text= "Create Pet")
        self.button1.grid(row= 2, column= 0, columnspan= 2, sticky="nsew")

        self.label3 = Label(root, text= "Units")
        self.label3.grid(row= 3, column= 0, sticky="nsew")

        self.entry3 = Entry(root)
        self.entry3.grid(row= 3, column= 1, sticky="nsew")

        self.button2 = Button(root, text= "Feed")
        self.button2.grid(row= 4, column= 0, sticky="nsew")

        self.button3 = Button(root, text= "Exercise")
        self.button3.grid(row= 4, column= 1, sticky="nsew")

        self.label4 = Label(root, text= "Create a pet to begin.")
        self.label4.grid(row= 5, column= 0, columnspan= 2, sticky="nsew")

        for i in range(6): root.rowconfigure(i, weight=1)
        for i in range(2): root.columnconfigure(i, weight=1)


if __name__ == "__main__":
    root = Tk()
    app = PetGUI(root)
    root.mainloop()