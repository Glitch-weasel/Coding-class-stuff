from tkinter import *

ABS_Z_F = -459.67
ABS_Z_C = -273.15

font_Main_Title = "Veranda 16 bold"
font_Heading = "Veranda 12 bold"
font_Default = "Veranda 12"

class TemperatureConverter:

    def F_to_C(self, temp):
        try:
            temp = float(temp)
            if temp >= ABS_Z_F:
                result = (float(temp)-32) * 5 / 9
                return f'{result:.1f} degrees Centigrade'
            else:
                return "temperature too low"
        except ValueError:
            return "Please enter a number"
        
    def C_to_f():
        try:
            temp = float(temp)
            if temp >= ABS_Z_C:
                result = (float(temp)+32) / 5 * 9
                return f'{result:.1f} degrees Fahrenheit'
            else:
                return "temperature too low"
        except ValueError:
            return "Please enter a number"

class ConverterGUI:
    def __init__(self, root):
        self.converter = TemperatureConverter()
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("400x150")


        self.container = Frame(self.root)
        self.container.grid(row= 0, column= 0, sticky= "nsew")


        self.frames = {}

        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_cFrame"] = self.create_to_c_frame()
        self.frames["to_fFrame"] = self.create_to_f_frame()

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainFrame")


    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()


    def create_main_frame(self):
        frame = Frame(self.container)

        Label(frame, font= "Veranda 16 bold", text= "Temperature converter"
            ).pack()

        Button(frame,
            text="F to C",
            command=lambda: self.show_frame("to_cFrame")
            ).pack()

        Button(frame,
            text="C to F",
            command=lambda: self.show_frame("to_fFrame")
            ).pack()
            
        return frame
        
    def create_to_c_frame(self):
        frame = Frame(self.container)

        Label(frame, font= "Veranda 16 bold", text= "Fahrenheit to Centigrade"
            ).pack()

        Button(frame,
            text="Home",
            command=lambda: self.show_frame("MainFrame")
            ).pack()

        return frame
        
    def create_to_f_frame(self):
        frame = Frame(self.container)

        Label(frame, font= "Veranda 16 bold", text= "Centigrade to Fahrenheit"
            ).pack()

        Button(frame,
            text="Home",
            command=lambda: self.show_frame("MainFrame")
            ).pack()

        return frame
    

if __name__ == "__main__":
    root = Tk()
    app = ConverterGUI(root)
    root.mainloop()