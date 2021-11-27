class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, mass, track):
        """масса в кг, длина пути в м"""
        res = self._length * self._width * mass * track
        print(res, 'кг')


road1 = Road(15, 6)
road1.mass(5, 2000)
