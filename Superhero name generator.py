from tkinter import *
from tkinter import ttk


root = Tk()
radio_var = StringVar()

class GUI:
    def print_name():
        
        return
    
    def labels():
        label1 = Label(root, text= "Hero Name Generator")
        label1.grid(row= 0)

        label2 = Label(root, text= "Choose an adjective...")
        label2.grid(row= 1)

        label3 = Label(root, text= "Enter a colour")
        label3.grid(row= 6)

        label4 = Label(root, text= "Pick an animal")
        label4.grid(row= 8)

        label5 = Label(root, text= f"You are the {hero_name}!")
        label5.grid(row= 11)

    def radiobuttons(radio_var):
        opt1 = ttk.Radiobutton(root, text= "Happy", value= "Happy", variable= radio_var)
        opt1.grid(row= 2)

        opt2 = ttk.Radiobutton(root, text= "Awesome", value= "Awesome", variable= radio_var)
        opt2.grid(row= 3)

        opt3 = ttk.Radiobutton(root, text= "Outgoing", value= "Outgoing", variable= radio_var)
        opt3.grid(row= 4)

        opt4 = ttk.Radiobutton(root, text= "Funky", value= "Funky", variable= radio_var)
        opt4.grid(row= 5)
    
    def entries_and_button():
        entry1 = Entry(root)
        entry1.grid(row= 7)

        entry2 = Entry(root)
        entry2.grid(row= 9)

        button = Button(root, text= "GO!", command=lambda: print_name())