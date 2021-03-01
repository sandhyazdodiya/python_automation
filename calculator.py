class Calculator:
    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        if a>b:
            return a-b
        return b-a

    def multiply(self, a, b):
        return a*b

    def mod(self, a, b):
        return a%b

    def divide(self, a, b):
        return a//b