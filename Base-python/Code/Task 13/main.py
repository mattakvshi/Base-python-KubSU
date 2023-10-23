import Shape
from C1 import C1
from C2 import C2
from C3 import C3


def change_position(shapes):
    while True:
        print("Желаете ли вы изменить местоположение какой-либо из фигур?")
        print("0 - нет, 1 - да")
        response = int(input())
        if response == 0:
            break
        elif response == 1:
            shape_name = input("Введите имя фигуры, местоположение которой вы хотите изменить: ")
            dx = float(input("Введите изменение по оси x: "))
            dy = float(input("Введите изменение по оси y: "))
            for shape in shapes:
                if shape.name == shape_name:
                    shape.move(dx, dy)
                    print("Местоположение фигуры успешно изменено.")
        else:
            print("Введен неверный вариант ответа. Введите 0 или 1.")


def change_color(shapes):
    while True:
        print("Желаете ли вы изменить цвет заливки какой-либо из фигур?")
        print("0 - нет, 1 - да")
        response = int(input())
        if response == 0:
            break
        elif response == 1:
            shape_name = input("Введите имя фигуры, цвет заливки которой вы хотите изменить: ")
            new_color = input("Введите новый цвет: ")
            for shape in shapes:
                if shape.name == shape_name:
                    shape.setFill(new_color)
                    print("Цвет заливки фигуры успешно изменен.")
        else:
            print("Введен неверный вариант ответа. Введите 0 или 1.")


def main():
    # Создание списка объектов
    shapes = [
        C1(1, 0, 5, "Красный", "Квадрат1"),
        C2(2, 2, 4, 3, "Синий", "Ромб1"),
        C3(1, 1, 2, 4, "Зеленый", "Прямоугольник1"),
        C1(-1, -1, 3, "Желтый", "Квадрат2"),
        C2(3, 3, 6, 2, "Фиолетовый", "Ромб2"),
        C3(2, 2, 3, 2, "Оранжевый", "Прямоугольник2"),
        C1(0, 0, 5, "Черный", "Квадрат3"),
        C2(2, 2, 4, 3, "Белый", "Ромб3"),
        C3(1, 1, 2, 4, "Серый", "Прямоугольник3"),
        C1(-1, -1, 3, "Темно-синий", "Квадрат4"),
        C2(3, 3, 6, 2, "Розовый", "Ромб4"),
        C3(2, 2, 3, 2, "Бирюзовый", "Прямоугольник4"),
        C1(0, 0, 4, "Золотой", "Квадрат5"),
        C2(2, 2, 5, 4, "Серебристый", "Ромб5"),
        C3(1, 1, 3, 4, "Бежевый", "Прямоугольник5")
    ]

    # Удаление дубликатов объектов
    unique_shapes = list(set(shapes))

    # Вывод информации о каждом объекте
    for shape in unique_shapes:
        print(f"Фигура: {type(shape).__name__}")
        print((f"Название: {shape.name}"))
        print(f"Площадь: {shape.square()}")
        print(f"Периметр: {shape.perimeter()}")
        try:
            print(f"Цвет заливки: {shape.color}")
        except AttributeError:
            print("Цвет заливки не установлен")
        print()


    change_position(unique_shapes)
    change_color(unique_shapes)


    # Сравнение фигур по площади
    for i in range(len(unique_shapes)):
        for j in range(i + 1, len(unique_shapes)):
            print(
                f"Сравниваем {type(unique_shapes[i]).__name__}, {unique_shapes[i].name} и {type(unique_shapes[j]).__name__}, {unique_shapes[j].name}:")
            print(unique_shapes[i].compare(unique_shapes[j]))
            print()

    # Определение факта пересечения фигур и включения
    for i in range(len(unique_shapes)):
        for j in range(i + 1, len(unique_shapes)):
            print(
                f"{type(unique_shapes[i]).__name__}, {unique_shapes[i].name}  пересекается с {type(unique_shapes[j]).__name__}, {unique_shapes[j].name}:")
            print(unique_shapes[i].is_intersect(unique_shapes[j]))
            print()
            print(
                f"{type(unique_shapes[i]).__name__}, {unique_shapes[i].name} включает {type(unique_shapes[j]).__name__}, {unique_shapes[j].name}:")
            print(unique_shapes[i].is_include(unique_shapes[j]))
            print()


main()
