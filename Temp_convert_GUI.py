from tkinter import *

ABS_Z_F = -459.67
ABS_Z_C = -273.15

font_Main_Title = ("Verdana", 20, "bold")
font_Heading = ("Verdana", 14, "bold")
font_Default = ("Verdana", 12)


class TemperatureConverter:

    def F_to_C(self, temp):
        try:
            temp = float(temp)

            if temp >= ABS_Z_F:
                result = (temp - 32) * 5 / 9
                return f"{result:.1f} °C"
            else:
                return "Temperature too low"

        except ValueError:
            return "Please enter a number"

    def C_to_F(self, temp):
        try:
            temp = float(temp)

            if temp >= ABS_Z_C:
                result = (temp * 9 / 5) + 32
                return f"{result:.1f} °F"
            else:
                return "Temperature too low"

        except ValueError:
            return "Please enter a number"


class ConverterGUI:

    def __init__(self, root):

        self.converter = TemperatureConverter()

        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("500x250")

        # Make window responsive
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_cFrame"] = self.create_to_c_frame()
        self.frames["to_fFrame"] = self.create_to_f_frame()

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainFrame")

    def show_frame(self, name):
        self.frames[name].tkraise()

    # ---------------- Main Menu ---------------- #

    def create_main_frame(self):

        frame = Frame(self.container)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        Label(
            frame,
            text="Temperature Converter",
            font=font_Main_Title
        ).grid(row=0, column=0, columnspan=2, pady=20)

        Button(
            frame,
            text="to Centigrade",
            font=font_Heading,
            bg="purple",
            width=15,
            height=3,
            command=lambda: self.show_frame("to_cFrame")
        ).grid(row=1, column=0, padx=10, pady=20, sticky="nsew")

        Button(
            frame,
            text="to Fahrenheit",
            font=font_Heading,
            bg="orange",
            width=15,
            height=3,
            command=lambda: self.show_frame("to_fFrame")
        ).grid(row=1, column=1, padx=10, pady=20, sticky="nsew")

        return frame

    # ---------------- F to C ---------------- #

    def create_to_c_frame(self):

        frame = Frame(self.container)

        for i in range(4):
            frame.grid_rowconfigure(i, weight=1)

        for i in range(3):
            frame.grid_columnconfigure(i, weight=1)

        Label(
            frame,
            text="Enter the temperature in Fahrenheit",
            font=font_Heading
        ).grid(row=0, column=0, columnspan=3, pady=10)

        self.entry_f = Entry(frame, font=font_Default, justify="center")
        self.entry_f.grid(row=1, column=0, columnspan=3, sticky="ew")

        Button(
            frame,
            text="Calculate",
            font=font_Default,
            command=self.calculate_to_c
        ).grid(row=2, column=0, sticky="nsew")

        Button(
            frame,
            text="Back",
            font=font_Default,
            command=lambda: self.show_frame("MainFrame")
        ).grid(row=2, column=1, sticky="nsew")

        Button(
            frame,
            text="Reset",
            font=font_Default,
            command=self.reset_c
        ).grid(row=2, column=2, sticky="nsew")

        self.result_c = Label(
            frame,
            text="Converted temperature goes here",
            font=font_Default
        )
        self.result_c.grid(row=3, column=0,
                           columnspan=3, pady=10)

        return frame

    # ---------------- C to F ---------------- #

    def create_to_f_frame(self):

        frame = Frame(self.container)

        for i in range(4):
            frame.grid_rowconfigure(i, weight=1)

        for i in range(3):
            frame.grid_columnconfigure(i, weight=1)

        Label(
            frame,
            text="Enter the temperature in Centigrade",
            font=font_Heading
        ).grid(row=0, column=0, columnspan=3, pady=10)

        self.entry_c = Entry(frame, font=font_Default, justify="center")
        self.entry_c.grid(row=1, column=0, columnspan=3, sticky="ew")

        Button(
            frame,
            text="Calculate",
            font=font_Default,
            command=self.calculate_to_f
        ).grid(row=2, column=0, sticky="nsew")

        Button(
            frame,
            text="Back",
            font=font_Default,
            command=lambda: self.show_frame("MainFrame")
        ).grid(row=2, column=1, sticky="nsew")

        Button(
            frame,
            text="Reset",
            font=font_Default,
            command=self.reset_f
        ).grid(row=2, column=2, sticky="nsew")

        self.result_f = Label(
            frame,
            text="Converted temperature goes here",
            font=font_Default
        )
        self.result_f.grid(row=3, column=0,
                           columnspan=3, pady=10)

        return frame

    # ---------------- Calculations ---------------- #

    def calculate_to_c(self):
        value = self.entry_f.get()
        result = self.converter.F_to_C(value)
        self.result_c.config(text=result)

    def calculate_to_f(self):
        value = self.entry_c.get()
        result = self.converter.C_to_F(value)
        self.result_f.config(text=result)

    # ---------------- Reset Buttons ---------------- #

    def reset_c(self):
        self.entry_f.delete(0, END)
        self.result_c.config(text="Converted temperature goes here")

    def reset_f(self):
        self.entry_c.delete(0, END)
        self.result_f.config(text="Converted temperature goes here")


if __name__ == "__main__":
    root = Tk()
    app = ConverterGUI(root)
    root.mainloop()