from src_08.Tetragon import Tetragon
from typing import *
from PyQt5.QtCore import QPoint, QLineF


class Parallelogram(Tetragon):
    def __init__(self, points: List[QPoint]):
        super().__init__(points)
        a, b, c, d = self.edges
        angle1, angle2 = a.angleTo(c), b.angleTo(d)
        if angle1 not in [180.0, 0.0] or angle2 not in [180.0, 0.0]:
            raise Exception('Opposite sides are not parallel')


if __name__ == "__main__":
    points = [
        QPoint(0, 0),
        QPoint(10, 30),
        QPoint(40, 30),
        QPoint(30, 0),
    ]
    a = Parallelogram(points)
    print('Периметр: ', a.perimeter())
    print('Площадь: ', a.area())

