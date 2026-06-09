from tkinter import *


class TemperatureConverter:

    def F_to_C(self, temp):
        temp = float(temp)
        if temp >= -273.15:
            result = (float(temp)-32) * 5 / 9
            return f'{result:.1f} degrees Centigrade'
        else:
            return "temperature too low"