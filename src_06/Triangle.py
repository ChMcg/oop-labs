from PyQt5 import QtCore, QtGui, QtWidgets
from enum import Enum
from math import *

class TriangleType(Enum):
    RIGHT       = 0
    ISOSCELES   = 1
    EQUILATERAL = 2
    NONE        = 3

class Triangle(QtGui.QPolygon):
    def __init__(self, a, b, c, angle, offset: QtCore.QPoint = QtCore.QPoint(0, 0), tt: TriangleType = TriangleType.NONE):
        print('new triangle:', (a, b, c), 
                'angle:', angle, 
                'offset:', offset, 
                'selection:', tt)
        super().__init__(
                self.generate(
                    a, b, c, 
                    angle=angle,
                    offset=offset, 
                    tt=tt
                )
            )
       

    def generate(self, a, b, c, angle, offset: QtCore.QPoint = QtCore.QPoint(0, 0), tt: TriangleType = TriangleType.NONE):
        if tt is TriangleType.NONE:
            raise BaseException("Triangle type must be set")
        # if a + b < c or a + c < b or b + c < a:
        #     raise BaseException("Unreal triangle:", (a, b, c))
        ret = []
        if tt is TriangleType.RIGHT:
            ret = [
                offset + QtCore.QPoint(0, 0),
                offset + QtCore.QPoint(b, 0),
                offset + QtCore.QPoint(0, a)
            ]
        if tt is TriangleType.ISOSCELES:
            ret = [
                offset + QtCore.QPoint(0, 0),
                offset + QtCore.QPoint( a*sin(angle), a*cos(angle)),
                offset + QtCore.QPoint(-a*sin(angle), a*cos(angle))
            ]
        if tt is TriangleType.EQUILATERAL:
            angle = 60*pi/360
            ret = [
                offset + QtCore.QPoint(0, 0),
                offset + QtCore.QPoint( a*sin(angle), a*cos(angle)),
                offset + QtCore.QPoint(-a*sin(angle), a*cos(angle))
                # offset + QtCore.QPoint( a*sin(radians(60)), a*cos(radians(60))),
                # offset + QtCore.QPoint(-a*sin(radians(60)), a*cos(radians(60)))
            ]
        print('coordinates generated:', ret)
        return ret