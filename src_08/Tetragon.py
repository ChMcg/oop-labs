import math
from typing import *
from PyQt5.QtCore import QPoint, QLineF
from src_08.Polygon import Polygon


class Tetragon(Polygon):
    def __init__(self, points: List[QPoint]):
        if len(points) != 4:
            raise Exception('Tetragon needs exactly 4 points')
        super().__init__(points)
    
    def area(self) -> float:
        d1 = QLineF(self.points[0], self.points[2])
        d2 = QLineF(self.points[1], self.points[3])
        angle = d1.angleTo(d2)
        angle = math.radians(angle)
        d1 = d1.length()
        d2 = d2.length()
        return abs(d1*d2*math.sin(angle))


if __name__ == "__main__":
    points = [
        QPoint(0,   0),
        QPoint(30,  0),
        QPoint(30,  30),
        QPoint( 0,  30)
    ]
    a = Tetragon(points)
    print('Периметр: ', a.perimeter())
    print('Площадь: ', a.area())

