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