class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}*i'

    def __add__(self, other):
        return f'Сумма: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение: {self.a * other.a - self.b * other.b} + {self.b * other.a + self.a * other.b} * i'


z1 = ComplexNumber(1, 2)
z2 = ComplexNumber(2, 3)
print(z1 + z2)
print(z1 * z2)
print(z1)
