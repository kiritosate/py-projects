# console based basic-calculator
# simple OOP
# by: kiritosate

class Calculator:

    def __init__(self) -> None:
        
        result = None
        self.number1 = int(input("enter first number: "))
        self.number2 = int(input("enter second number: "))
        self.operator = input("enter ( + , - , *, /): ")

        if self.operator == '+':
            result = self.addition(self.number1, self.number2)
        elif self.operator == '-':
            result = self.minus(self.number1, self.number2)
        elif self.operator == '*':
            result = self.multiplication(self.number1, self.number2)
        elif self.operator == '/':
            result = self.division(self.number1, self.number2)
        else:
            print(ValueError)

        print(result)

    def addition(self, number1, number2):

        return number1 + number2
    
    def minus(self, number1, number2):

        return number1 - number2

    def multiplication(self, number1, number2):

        return number1 * number2
    
    def division(self, number1, number2):

        return number1 / number2

if __name__ == '__main__':

    Calculator()