class Calculator:
    PI = 3.1414
    
    @staticmethod
    def sum(num1, num2):
        return num1 + num2
    
    @staticmethod
    def circle_area(radio):
        return Calculator.PI * (radio ** 2)
