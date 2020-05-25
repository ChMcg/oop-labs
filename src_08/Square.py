from src_08.Rectangle import Rectangle
from src_08.Rhomb import Rhomb
from typing import *
from PyQt5.QtCore import QPoint, QLineF


class Square(Rectangle, Rhomb):
    def __init__(self, points: List[QPoint]):
        Rectangle.__init__(self, points)
        Rhomb.__init__(self, points)

    def area(self) -> float:
        a = self.edges[0].length()
        return a**2 

    def perimeter(self) -> float:
        a = self.edges[0].length()
        return 4*a 


if __name__ == "__main__":
    points = [
        QPoint( 0,  0),
        QPoint( 0, 30),
        QPoint(30, 30),
        QPoint(30,  0),
    ]
    a = Square(points)
    print('Периметр: ', a.perimeter())
    print('Площадь: ', a.area())

