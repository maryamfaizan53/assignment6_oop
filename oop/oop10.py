# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.
class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print( "Woah Woah Woah") 
        
dog1= Dog("Tommy", "puppy")
dog2= Dog("Jack", "bulldog")
print(f"{dog1.name} has a breed {dog1.breed} and {dog2.name} has a breed {dog2.breed}")
dog1.bark() 

                