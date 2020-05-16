from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Union, List, Tuple
from random import randint
from enum import Enum 

class DrawableType(Enum):
    POLYGON = 0
    CIRCLE  = 1
    ELLIPSE = 2
    GRID    = 3

class GridType(Enum):
    REGULAR = 0
    RANDOM  = 1

class Drawable():
    def __init__(self, d_type: DrawableType):
        self.type = d_type

    def draw(self, painter: QtGui.QPainter):
        pass


class Rectangle(Drawable):
    def __init__(self, sides: Tuple[int, int], offset: QtCore.QPoint):
        super().__init__(DrawableType.POLYGON)
        self.rect = self.generate(sides, offset)

    def draw(self, painter: QtGui.QPainter):
        painter.drawPolygon(QtGui.QPolygon(self.rect))

    def generate(self, sides: Tuple[int, int], offset: QtCore.QPoint) -> List[QtCore.QPoint]:
        a, b = sides
        ret = [
            offset + QtCore.QPoint(-a//2, -b//2),
            offset + QtCore.QPoint(-a//2,  b//2),
            offset + QtCore.QPoint( a//2,  b//2),
            offset + QtCore.QPoint( a//2, -b//2)
        ]
        return ret


class Square(Drawable):
    def __init__(self, side: int, offset: QtCore.QPoint):
        super().__init__(DrawableType.POLYGON)
        self.rect = self.generate(side, offset)

    def draw(self, painter: QtGui.QPainter):
        painter.drawPolygon(QtGui.QPolygon(self.rect))

    def generate(self, side: int, offset: QtCore.QPoint) -> List[QtCore.QPoint]:
        a = side
        ret = [
            offset + QtCore.QPoint(-a//2, -a//2),
            offset + QtCore.QPoint(-a//2,  a//2),
            offset + QtCore.QPoint( a//2,  a//2),
            offset + QtCore.QPoint( a//2, -a//2)
        ]
        return ret


class Circle(Drawable):
    def __init__(self, radius: int, offset: QtCore.QPoint):
        super().__init__(DrawableType.CIRCLE)
        self.rect = self.generate(radius, offset)

    def draw(self, painter: QtGui.QPainter):
        painter.drawEllipse(QtCore.QRect(*self.rect))

    def generate(self, radius: int, offset: QtCore.QPoint) -> List[QtCore.QPoint]:
        a = radius
        ret = [
            offset + QtCore.QPoint(-a, -a),
            offset + QtCore.QPoint( a,  a)
        ]
        return ret


class Ellipse(Drawable):
    def __init__(self, sides: Tuple[int, int], offset: QtCore.QPoint):
        super().__init__(DrawableType.ELLIPSE)
        self.rect = self.generate(sides, offset)

    def draw(self, painter: QtGui.QPainter):
        painter.drawEllipse(QtCore.QRect(*self.rect))

    def generate(self, sides: Tuple[int, int], offset: QtCore.QPoint) -> List[QtCore.QPoint]:
        a, b = sides
        ret = [
            offset + QtCore.QPoint(-a//2, -b//2),
            offset + QtCore.QPoint( a//2,  b//2)
        ]
        return ret


class RegularGrid(Drawable):
    def __init__(self, density: Tuple[int, int], window: QtCore.QRect):
        super().__init__(DrawableType.GRID)
        self.density_x, self.density_y = density
        area = window
        self.max_x, self.max_y = area.width(), area.height()
        h_x, h_y = self.max_x // self.density_x, self.max_y // self.density_y
        self.points_x = [i*h_x for i in range(self.max_x // h_x +1)]
        self.points_y = [i*h_y for i in range(self.max_y // h_y +1)]

    def draw(self, painter: QtGui.QPainter):
        for x in self.points_x:
            painter.drawLine(
                QtCore.QPoint(x,          0),
                QtCore.QPoint(x, self.max_y)
            )
        for y in self.points_y:
            painter.drawLine(
                QtCore.QPoint(         0, y),
                QtCore.QPoint(self.max_x, y)
            )


class RandomGrid(Drawable):
    def __init__(self, density: Tuple[int, int], window: QtCore.QRect):
        super().__init__(DrawableType.GRID)
        self.density_x, self.density_y = density
        area = window
        self.max_x, self.max_y = area.width(), area.height()
        self.h_x, self.h_y = self.max_x // self.density_x, self.max_y // self.density_y
        self.points_x = [randint(0, self.max_x) for _ in range(self.max_x // self.h_x +1)]
        self.points_y = [randint(0, self.max_y) for _ in range(self.max_y // self.h_y +1)]

    def draw(self, painter: QtGui.QPainter):
        for x in self.points_x:
            painter.drawLine(
                QtCore.QPoint(x,          0),
                QtCore.QPoint(x, self.max_x)
            )
        for y in self.points_y:
            painter.drawLine(
                QtCore.QPoint(         0, y),
                QtCore.QPoint(self.max_y, y)
            )




        

