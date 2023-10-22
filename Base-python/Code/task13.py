import math

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
            return "The areas are equal."
        elif self.square() > other.square():
            return "The first shape is larger."
        else:
            return "The second shape is larger."

    def is_intersect(self, other):
        return (other.x >= self.x and other.y >= self.y) or (self.x >= other.x and self.y >= other.y)

    def is_include(self, other):
        return (other.x >= self.x and other.y >= self.y) and (other.x + other.square() <= self.x + self.square() and other.y + other.square() <= self.y + self.square())


class C1(Shape): #Квадрат
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def square(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class C2(Shape): #Ромб
    def __init__(self, x, y, base, height):
        super().__init__(x, y)
        self.base = base
        self.height = height

    def square(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return 2 * self.base + 2 * self.height


class C3(Shape): #Прямоугольник
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * self.a + 2 * self.b


# Создание списка объектов
shapes = [
    C1(0, 0, 5),
    C2(2, 2, 4, 3),
    C3(1, 1, 2, 4),
    C1(-1, -1, 3),
    C2(3, 3, 6, 2),
    C3(2, 2, 3, 2),
    C1(0, 0, 5),
    C2(2, 2, 4, 3),
    C3(1, 1, 2, 4),
    C1(-1, -1, 3),
    C2(3, 3, 6, 2),
    C3(2, 2, 3, 2),
    C1(0, 0, 4),
    C2(2, 2, 5, 4),
    C3(1, 1, 3, 4)
]

# Удаление дубликатов объектов
unique_shapes = list(set(shapes))

# Вывод информации о каждом объекте
for shape in unique_shapes:
    print(f"Shape: {type(shape).__name__}")
    print(f"Square: {shape.square()}")
    print(f"Perimeter: {shape.perimeter()}")
    try:
        print(f"Fill color: {shape.color}")
    except AttributeError:
        print("No fill color")
    print()

# Сравнение фигур по площади
for i in range(len(unique_shapes)):
    for j in range(i+1, len(unique_shapes)):
        print(f"Comparing {type(unique_shapes[i]).__name__} and {type(unique_shapes[j]).__name__}:")
        print(unique_shapes[i].compare(unique_shapes[j]))
        print()

# Определение факта пересечения фигур и включения
for i in range(len(unique_shapes)):
    for j in range(i+1, len(unique_shapes)):
        print(f"{type(unique_shapes[i]).__name__} intersects {type(unique_shapes[j]).__name__}:")
        print(unique_shapes[i].is_intersect(unique_shapes[j]))
        print()
        print(f"{type(unique_shapes[i]).__name__} includes {type(unique_shapes[j]).__name__}:")
        print(unique_shapes[i].is_include(unique_shapes[j]))
        print()