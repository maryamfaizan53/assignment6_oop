# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count

class Counter:
    count = 0  # class variable to keep track of object count

    def __init__(self):
        Counter.count += 1  # increment the count whenever a new object is created

    @classmethod
    def display_count(cls):  # class method to display the count
        print(f"Number of objects created: {cls.count}")
        
# creating objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()


# calling class method to display count
Counter.display_count()  # Output: Number of objects created: 3
        