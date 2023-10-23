from Shape import Shape


class C3(Shape): #Прямоугольник
    def __init__(self, x, y, a, b, color, name):
        super().__init__(x, y, color, name)
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * self.a + 2 * self.b
