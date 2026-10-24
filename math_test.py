import math

class MathOperations:
    def __init__(self):
        pass

    def sprt(self, x):
        print(math.sqrt(x))

    def square(self, x):
        print(math.pow(x, int(input("Enter the power: "))))

    def pi(self):
        print(math.pi)

    def log(self, x):
        print(math.log(x,int(input("Enter the power: "))))

    def factorial(self, input_x):
        input_x = int(input("Enter a number to calculate its factorial: "))
        print(math.factorial(input_x))

math_test = MathOperations()

math_test.sprt(16)
math_test.square(5)
math_test.pi()
math_test.log(10)
math_test.factorial(5)
