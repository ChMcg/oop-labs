from src_08.Parallelogram import Parallelogram
from typing import *
from PyQt5.QtCore import QPoint, QLineF


class Rectangle(Parallelogram):
    def __init__(self, points: List[QPoint]):
        super().__init__(points)
        a, b, c, d = [x.length() for x in self.edges]
        if a != c or b != d:
            raise Exception('Opposite sides are not equal')

    def area(self) -> float:
        a, b = [x.length() for x in self.edges[0:2]]
        return a*b
    
    def perimeter(self) -> float:
        a, b = [x.length() for x in self.edges[0:2]]
        return 2*a + 2*b

if __name__ == "__main__":
    points = [
        QPoint( 0,  0),
        QPoint( 0, 30),
        QPoint(40, 30),
        QPoint(40,  0),
    ]
    a = Rectangle(points)
    print('Периметр: ', a.perimeter())
    print('Площадь: ', a.area())



        