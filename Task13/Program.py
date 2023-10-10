from C1 import  C1
from C2 import C2
from C3 import C3


class Program:
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
        print(f"Фигура: {type(shape).__name__}")
        print(f"Площадь: {shape.square()}")
        print(f"Периметер: {shape.perimeter()}")
        try:
            print(f"Цвет заливки: {shape.color}")
        except AttributeError:
            print("Цвет заливки не задан")
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
            print(f"{type(unique_shapes[i]).__name__} включает {type(unique_shapes[j]).__name__}:")
            print(unique_shapes[i].is_include(unique_shapes[j]))
            print()