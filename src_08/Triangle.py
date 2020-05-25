from src_08.Polygon import Polygon
from typing import *
import math
from PyQt5.QtCore import QPoint, QLineF



class Triangle(Polygon):
    def __init__(self, points: List[QPoint]):
        if len(points) != 3:
            raise Exception('Triangle needs exactly 3 points')
        super().__init__(points)

    def area(self) -> float:
        p = self.perimeter()/2
        a, b, c = [x.length() for x in self.edges]
        return math.sqrt(p*(p-a)*(p-b)*(p-c))


if __name__ == "__main__":
    points = [
        QPoint(0,   0),
        QPoint(30,  0),
        QPoint(30,  30)
    ]
    a = Triangle(points)
    print(a)
    print('Периметр: ', a.perimeter())
    print('Площадь: ', a.area())