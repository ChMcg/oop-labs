from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Union, List, Tuple
from random import randint
from enum import Enum 

class DrawableType(Enum):
    RECTANGLE   = 0
    SQUARE      = 1
    CIRCLE      = 2
    ELLIPSE     = 3
    GRID        = 4

class GridType(Enum):
    REGULAR = 0
    RANDOM  = 1

class Drawable():
    def __init__(self, d_type: DrawableType):
        self.type = d_type

    def draw(self, painter: QtGui.QPainter):
        raise NotImplementedError()

    def contains(self, point: QtCore.QPoint):
        raise NotImplementedError()


class Rectangle(Drawable):
    def __init__(self, sides: Tuple[int, int], offset: QtCore.QPoint):
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

    def contains(self, point: QtCore.QPoint):
        rect = self.rect[0], self.rect[2]
        return QtCore.QRect(*rect).contains(point)


class Square(Drawable):
    def __init__(self, side: int, offset: QtCore.QPoint):
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

    def contains(self, point: QtCore.QPoint):
        rect = self.rect[0], self.rect[2]
        return QtCore.QRect(*rect).contains(point)


class Circle(Drawable):
    def __init__(self, radius: int, offset: QtCore.QPoint):
        self.rect = self.generate(radius, offset)
        self.center = offset
        self.radius = radius

    def draw(self, painter: QtGui.QPainter):
        painter.drawEllipse(QtCore.QRect(*self.rect))

    def generate(self, radius: int, offset: QtCore.QPoint) -> List[QtCore.QPoint]:
        a = radius
        ret = [
            offset + QtCore.QPoint(-a, -a),
            offset + QtCore.QPoint( a,  a)
        ]
        return ret

    def contains(self, point: QtCore.QPoint):
        return QtCore.QLineF(self.center, point).length() < self.radius


class Ellipse(Drawable):
    def __init__(self, sides: Tuple[int, int], offset: QtCore.QPoint):
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


class Figure():
    def __init__(self, offset: QtCore.QPoint, dt: DrawableType, a: int, b: int = 0, radius: int = 0):
        if dt is DrawableType.RECTANGLE:
            self.figure = Rectangle([a, b], offset)
        elif dt is DrawableType.SQUARE:
            self.figure = Square(a, offset)
        elif dt is DrawableType.CIRCLE:
            self.figure = Circle(radius, offset)
        elif dt is DrawableType.ELLIPSE:
            self.figure = Ellipse([a, b], offset)
    
    def draw(self, painter: QtGui.QPainter):
        self.figure.draw(painter)

    def contains(self, point: QtCore.QPoint):
        return self.figure.contains(point)


class RegularGrid():
    def __init__(self, density: Tuple[int, int], window: QtCore.QRect):
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

    def intersect(self, objects: List[Figure]) -> Tuple[int, int]:
        total = len(self.points_x) * len(self.points_y)
        free = total
        points : List[QtCore.QPoint] = [QtCore.QPoint(x, y) for x in self.points_x for y in self.points_y]
        visited : List[bool] = [False for _ in points]
        for i, obj in enumerate(objects):
            for j, point in enumerate(points):
                if not visited[j] and obj.contains(point):
                    free -= 1
                    visited[j] = True
        return (free, total)


class RandomGrid():
    def __init__(self, density: Tuple[int, int], window: QtCore.QRect):
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

    def intersect(self, objects: List[Figure]) -> Tuple[int, int]:
        total = len(self.points_x) * len(self.points_y)
        free = total
        points : List[QtCore.QPoint] = [QtCore.QPoint(x, y) for x in self.points_x for y in self.points_y]
        visited : List[bool] = [False for _ in points]
        for i, obj in enumerate(objects):
            for j, point in enumerate(points):
                if not visited[j] and obj.contains(point):
                    free -= 1
                    visited[j] = True
        return (free, total)


class Grid(RegularGrid, RandomGrid):
    def __init__(self, density: Tuple[int, int], window: QtCore.QRect, gt: GridType):
        if gt is GridType.REGULAR:
            RegularGrid.__init__(self, density, window)
        elif gt is GridType.RANDOM:
            RandomGrid.__init__(self, density, window)
        else:
            raise BaseException('Unknown grid type:', gt)





