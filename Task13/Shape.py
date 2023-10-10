class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        pass

    def perimeter(self):
        pass

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def fill(self, color):
        self.color = color

    def compare(self, other):
        if self.square() == other.square():
            return "Фигуры равны"
        elif self.square() > other.square():
            return "Первая фигура больше."
        else:
            return "Вторая фгура больше."

    def is_intersect(self, other):
        return (other.x >= self.x and other.y >= self.y) or (self.x >= other.x and self.y >= other.y)

    def is_include(self, other):
        return (other.x >= self.x and other.y >= self.y) and (other.x + other.square() <= self.x + self.square() and other.y + other.square() <= self.y + self.square())