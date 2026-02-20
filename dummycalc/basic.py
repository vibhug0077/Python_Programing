"""Basic arithmetic operations."""
class basic():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return(self.a +self.b)

    def add(a, b):
        return a + b

    def Pratishta(Q):
        return("Voooh")

    def subtract(a, b):
        return a - b


    def multiply(a, b):
        return a * b


    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
