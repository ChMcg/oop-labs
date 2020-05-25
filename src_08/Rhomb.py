from src_08.Parallelogram import Parallelogram
from typing import *
from PyQt5.QtCore import QPoint, QLineF


class Rhomb(Parallelogram):
    def __init__(self, points: List[QPoint]):
        super().__init__(points)
        edge_lengths = [x.length() for x in self.edges]
        if len(set(edge_lengths)) != 1:
            raise Exception('Length of edges are not equal')


if __name__ == "__main__":
    points = [
        QPoint( 0,  0),
        QPoint( 0, 30),
        QPoint(30, 30),
        QPoint(30,  0),
    ]
    a = Rhomb(points)
    print('Периметр: ', a.perimeter())
    print('Площадь: ', a.area())

