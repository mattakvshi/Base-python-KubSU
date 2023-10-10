from Shape import Shape

class C2(Shape): #Ромб
    def __init__(self, x, y, base, height):
        super().__init__(x, y)
        self.base = base
        self.height = height

    def square(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return 2 * self.base + 2 * self.height