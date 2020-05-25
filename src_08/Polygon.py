from typing import *
from PyQt5.QtCore import QPoint, QLineF


class Polygon():
    def __init__(self, points: List[QPoint]):
        self.points = points
        self.deg = len(self.points)
        self.edges = []
        for i in range(1, len(self.points)):
            self.edges.append(
                QLineF(
                    self.points[i],
                    self.points[i-1]
                )
            )
        self.edges.append(QLineF(self.points[-1], self.points[0]))

    def perimeter(self) -> float:
        ret = 0.0
        for edge in self.edges:
            ret += edge.length()
        return ret

    def area(self) -> float:
        raise NotImplementedError()

    def __str__(self) -> str:
        return '\n'.join([str(x) for x in self.edges])


if __name__ == "__main__":
    points = [
        QPoint(0,   0),
        QPoint(30,  0),
        QPoint(30,  30),
        QPoint( 0,  30)
    ]
    a = Polygon(points)
    print(a)
    print('Сторон:', a.deg)
    print('Периметр:', a.perimeter())
