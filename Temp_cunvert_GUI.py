from tkinter import *


font_Main_Title = "Veranda 16 bold"
font_Heading = "Veranda 12 bold"
font_Default = "Veranda 12"

class TemperatureConverter:

    def F_to_C(self, temp):
        temp = float(temp)
        if temp >= -273.15:
            result = (float(temp)-32) * 5 / 9
            return f'{result:.1f} degrees Centigrade'
        else:
            return "temperature too low"
        
    def C_to_f():
        temp = float(temp)
        if temp >= -459.67:
            result = (float(temp)+32) / 5 * 9
            return f'{result:.1f} degrees Fahrenheit'
        else:
            return "temperature too low"