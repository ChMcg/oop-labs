from src_08.Polygon import Polygon
from src_08.Triangle import Triangle
from src_08.Tetragon import Tetragon
from src_08.Rectangle import Rectangle
from src_08.Parallelogram import Parallelogram
from src_08.Rhomb import Rhomb
from src_08.Square import Square

from typing import *
from PyQt5.QtCore import QPoint


def menu() -> str:
    ret = []
    ret.append("1. Многоугольник")
    ret.append("2. Треугольник")
    ret.append("3. Четырёхугольник")
    ret.append("4. Прямоугольник")
    ret.append("5. Параллелограмм")
    ret.append("6. Ромб")
    ret.append("7. Квадрат")
    return '\n'.join(ret)


def scan_points(num: int) -> List[QPoint]:
    print('Вводите точки в формате [x, y]')
    ret = []
    for i in range(num):
        a = input(f'[{i+1}] >> ')
        a = a.replace('[', '').replace(']', '')
        point = [int(x.strip()) for x in a.split(',')]
        if len(point) != 2:
            raise Exception('Не удалось распознать точку')
        ret.append(QPoint(*point))
    return ret

def print_about(obj: Polygon):
    print(obj)
    print('Периметр:', obj.perimeter())
    if not obj is Polygon: 
        print('Площадь:', obj.area())

def polygon():
    print('Укажите количество вершин:')
    i = int(input('>>> '))
    points = scan_points(i)
    a = Polygon(points)
    print_about(a)

def triangle():
    points = scan_points(3)
    a = Triangle(points)
    print_about(a)
    
def tetragon():
    points = scan_points(4)
    a = Tetragon(points)
    print_about(a)

def rectangle():
    points = scan_points(4)
    a = Rectangle(points)
    print_about(a)

def parallelogram():
    points = scan_points(4)
    a = Parallelogram(points)
    print_about(a)

def rhomb():
    points = scan_points(4)
    a = Rhomb(points)
    print_about(a)

def square():
    points = scan_points(4)
    a = Square(points)
    print_about(a)


class MyApp():
    def exec(self) -> int:
        idle = True
        while idle:
            print('\n\n')
            print(menu())
            a = int(input('>>> '))
            if a == 1: polygon()
            if a == 2: triangle()
            if a == 3: tetragon()
            if a == 4: rectangle()
            if a == 5: parallelogram()
            if a == 6: rhomb()
            if a == 7: square()
        return 0


if __name__ == "__main__":
    a = MyApp()
    a.exec()
