# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathsUtils:
    @staticmethod
    def add(a,b):  #static method means hme __initr__lagane ki zrurt nhi# isme object bnane ki bhi zrurt nhi
        return a+b
    
result = MathsUtils.add(5, 3)
print(f"The sum is: {result}")
    