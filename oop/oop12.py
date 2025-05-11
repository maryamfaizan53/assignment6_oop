# Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class Temperature:
    def __init__ (self):
        pass
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
#@staticmethod → is decorator se method class ke andar hota hai, lekin self ya cls use nahi karta.

# Matlab: iska object banane ki zarurat nahi hoti — direct class se call kar sakte ho.

# Formula: F = (C × 9/5) + 32



temp_c = 25
temp_f = Temperature.celsius_to_fahrenheit(temp_c)

print(f"{temp_c}°C is equal to {temp_f}°F")