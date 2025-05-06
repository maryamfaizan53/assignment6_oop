# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Students:
    school = "Abc Schoool" # class attributes
    def __init__(self,name,marks): #constructors
       self.name = name
       self.marks = marks# object attributes
        
    def Details(self):
        print(f"Name: {self.name}, Marks: {self.marks} , School: {self.school}") # method to print details
        
student1 = Students("John", 90)    # object
student2 = Students("Mary", 95)    # object
student3 = Students("Sam", 85)    # object
student4 = Students("Anna", 88)    # object    


student1.Details() # calling method
student2.Details()# calling method
student3.Details() # calling method
student4.Details() # calling method
        
#     class Students:
#     school = "Abc School"  # class attribute

#     def __init__(self, name, marks):  # constructor
#         self.name = name  # object attribute
#         self.marks = marks  # object attribute

#     def Details(self):  # method to print details
#         print(f"Name: {self.name}, Marks: {self.marks}, School: {self.school}")

# # creating objects
# student1 = Students("John", 90)
# student2 = Students("Mary", 95)
# student3 = Students("Sam", 85)
# student4 = Students("Anna", 88)

# # calling method
# student1.Details()
# student2.Details()
# student3.Details()
# student4.Details()
