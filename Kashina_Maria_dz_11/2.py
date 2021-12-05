class DivisionByZero:
    def __init__(self, dividend, denominator):
        self.dividend = dividend
        self.denominator = denominator

    @staticmethod
    def division(dividend, denominator):
        try:
            return dividend / denominator
        except ZeroDivisionError:
            return f'Division by zero'


print(DivisionByZero.division(24, 0))
print(DivisionByZero.division(24, 6))
