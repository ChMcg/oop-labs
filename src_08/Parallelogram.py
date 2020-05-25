from src_08.Tetragon import Tetragon
from typing import *
from PyQt5.QtCore import QPoint, QLineF


class Parallelogram(Tetragon):
    def __init__(self, points: List[QPoint]):
        if len(points) != 4:
            raise Exception('Parallelogram needs exactly 4 points')
        a, b, c, d = [
            QLineF(points[0], points[1]),
            QLineF(points[1], points[2]),
            QLineF(points[2], points[3]),
            QLineF(points[3], points[0]),
        ]
        angle1, angle2 = a.angleTo(c), b.angleTo(d)
        if angle1 not in [180.0, 0.0] or angle2 not in [180.0, 0.0]:
            raise Exception('Opposite sides are not parallel')
        super().__init__(points)


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

