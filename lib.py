from math import pi


def rectangle_area(width, height):
    """Возвращает площадь прямоугольника по ширине и высоте."""
    return width * height


def rectangle_perimeter(width, height):
    """Возвращает периметр прямоугольника по ширине и высоте."""
    return 2 * (width + height)


def square_area(side):
    """Возвращает площадь квадрата по длине его стороны."""
    return side ** 2


def square_perimeter(side):
    """Возвращает периметр квадрата по длине его стороны."""
    return 4 * side


def circle_area(radius):
    """Возвращает площадь круга по его радиусу."""
    return pi * radius ** 2


def circle_perimeter(radius):
    """Возвращает длину окружности по её радиусу."""
    return 2 * pi * radius


def triangle_area(base, height):
    """Возвращает площадь треугольника по основанию и высоте к нему."""
    return base * height / 2


def triangle_perimeter(a, b, c):
    """Возвращает периметр треугольника по длинам его трёх сторон."""
    return a + b + c