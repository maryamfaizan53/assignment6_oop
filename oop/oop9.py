# Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().
from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height): # class atributes
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height    
    
obj = Rectangle(5, 10)
print(obj.area())  # Output: 50
#@abstractmethod ka matlab hai ke har subclass ko area() method lazmi implement karna hoga.
#abc ka matlab hai: Abstract Base Classes
#abstract class bnane k lye abc module import krna lazmi hai
#abstract method mai hm fucction ya method ko define krte hain jo ke kisi bhi class mai implement nahi hota
#abstract class mai hm sirf method ko define krte hain
#abstract class ko inherit krne wali class ko abstract method ko implement krna hota hai



                