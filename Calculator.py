class Calculator:
    def __init__(self):
        pass
    def add(self, x1, x2):
        return x1+x2
    def muliply(self, x1, x2):
        return x1*x2
    def subtruct(self, x1, x2):
        return x1-x2
    def divide(self, x1, x2):
        if x2 ==0:
            print("делить на ноль нельзя")
        else: return x1/x2