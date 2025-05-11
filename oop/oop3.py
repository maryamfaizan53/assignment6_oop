# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"The {self.brand} car is starting.")
        return True
    
car1 = Car("Toyota")
car2 = Car("Honda")

car1.start()  # Output: The Toyota car is starting.
car2.start()  # Output: The Honda car is starting.