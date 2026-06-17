from tkinter import *

OVERWEIGHT = 200
DANGEROUS = 300

class Pet:
    def __init__(self, name=None, weight=0):
        self.name = name.title()
        self.weight = weight
        self.dead = False

    def feed(self, units):
        if not self.dead:
            self.weight += units

            if self.weight > DANGEROUS:
                self.dead = True
            
            elif self.weight == DANGEROUS:
                    self.status.config(text=f"{self.name} is severely overweight and it's impacting their health. Exercise is advised immediately.  :(")
            
            else:
                if self.weight >= OVERWEIGHT:
                    self.status.config(text=f"{self.name} is overweight, why not help them get more fit?  :)")

    def exercise(self, units):
        if not self.dead:
            self.weight -= units

            if self.weight <= 0:
                self.dead = True

    def __str__(self):
        if self.dead:
            return f"{self.name} is dead."
        else:
            return f"{self.name} weighs {self.weight} units."


class PetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Pet")

        self.pet = None

        Label(root, text="Pet Name").grid(row=0, column=0)

        self.entry_name = Entry(root)
        self.entry_name.grid(row=0, column=1)

        Label(root, text="Starting Weight").grid(row=1, column=0)

        self.entry_weight = Entry(root)
        self.entry_weight.grid(row=1, column=1)

        Button(root, text="Create Pet", command=self.create_pet).grid(row=2, column=0, columnspan=2, sticky="nsew")

        Label(root, text="Units").grid(row=3, column=0)

        self.entry_units = Entry(root)
        self.entry_units.grid(row=3, column=1)

        Button(root, text="Feed", command=self.feed_pet).grid(row=4, column=0, sticky="nsew")

        Button(root, text="Exercise", command=self.exercise_pet).grid(row=4, column=1, sticky="nsew")

        self.status = Label(root, text="Create a pet to begin.")
        self.status.grid(row=5, column=0, columnspan=2)

    def create_pet(self):
        try:
            name = self.entry_name.get()
            weight = int(self.entry_weight.get())

            self.pet = Pet(name, weight)

            self.status.config(text=str(self.pet))

        except ValueError:
            self.status.config(text="Enter a valid weight.")

    def feed_pet(self):
        if self.pet is None:
            self.status.config(text="Create a pet first.")
            return

        try:
            units = int(self.entry_units.get())

            self.pet.feed(units)

            self.status.config(text=str(self.pet))

        except ValueError:
            self.status.config(text="Enter a valid number.")

    def exercise_pet(self):
        if self.pet is None:
            self.status.config(text="Create a pet first.")
            return

        try:
            units = int(self.entry_units.get())

            self.pet.exercise(units)

            self.status.config(text=str(self.pet))

        except ValueError:
            self.status.config(text="Enter a valid number.")


if __name__ == "__main__":
    root = Tk()
    app = PetGUI(root)
    root.mainloop()