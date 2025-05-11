# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Old Bank Name"
    
    def __init__(self,customer_name):    
        self.customer_name = customer_name
    
    @classmethod
    def change_bank_name(cls, name): 
        cls.bank_name = name
     
        def display(self): 
            print(f"Customer Name: {self.customer_name}, Bank Name: {self.bank_name}")    
     
#creating instance
customer1 = Bank("Maryam")
customer2 = Bank("faizan")   

# Displaying initial bank name
customer1.display()
customer2.display()  

#changing bank name using class methods
Bank.change_bank_name("New Bank Name")
# Displaying updated bank name
customer1.display()
customer2.display()