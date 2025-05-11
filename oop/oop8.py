#Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.
class Person:
    def __init__(self,name):
        self.name= name
        
class Teacher(Person):
    
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject= subject
        print(f"{self.name} is a teacher of {self.subject}")  
teacher1= Teacher("Miss Maryam","Maths") 
teacher2= Teacher("Mr Faiza","Physics")       
              