# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.
class Employee:
    def __init__(self,name,salary,ssn):
        self.name= name #public
        self._salary = salary #protected
        self.__ssn = ssn #private
      
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")
        
        #creating an instance of Employee
emp1 = Employee("John Doe", 50000, "00000000000")  

    
emp1.display()
# Accessing public variable
print(f"Public Name: {emp1.name}")

# Accessing protected variable
print(f"Protected Salary: {emp1._salary}")
# Accessing private variable (will raise an error)
try:
    print(f"Private SSN: {emp1.__ssn}")
except AttributeError as e:
    print(f"Error: {e}")
# Accessing private variable using name mangling
print(f"Private SSN (name mangling): {emp1._Employee__ssn}")
    