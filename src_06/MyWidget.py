from PyQt5 import QtCore, QtGui, QtWidgets
from src_06.Triangle import Triangle, TriangleType
from typing import List, Tuple
from enum import Enum
from math import pi


class MyWidget(QtWidgets.QWidget):
    def __init__(self, some):
        super().__init__(some)
        self.triangles : List[Triangle] = []
        self.preview : Triangle = None
        self.setMouseTracking(True)
        self.mainPen = QtGui.QPen(QtGui.QColor(0x0d, 0x47, 0xa1), 3)
        self.tempPen = QtGui.QPen(QtGui.QColor(0x0d, 0x47, 0xa1), 1)
        self.brush = QtGui.QBrush(QtGui.QColor(0x0d, 0x47, 0xa1), QtCore.Qt.Dense7Pattern)
        self.current_selection = TriangleType.NONE
        self.current_triangle : Tuple[3] = None
        self.current_angle : float = None

    def update_current_triangle(self, triangle: Tuple[int, int, int], angle: int):
        self.current_triangle = triangle
        self.current_angle = angle*pi/360
    
    def paintEvent(self, event: QtGui.QPaintEvent):
        print('objects:', self.triangles)
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setPen(self.mainPen)
        painter.setFont(QtGui.QFont('Decorative', 10))
        for triangle in self.triangles:
            painter.setBrush(self.brush)
            painter.drawPolygon(triangle)
            painter.setBrush(QtCore.Qt.NoBrush)
        if self.preview:
            painter.setPen(self.tempPen)
            painter.drawPolygon(self.preview)
        painter.end()

    def add_triangle(self, a, b, c):
        self.triangles.append(Triangle(a, b, c))

    def cleanup(self):
        self.triangles.clear()
        self.repaint()

    def updateSelection(self, selection: TriangleType):
        self.current_selection = selection

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        print('Mouse move event')
        if self.current_angle is None:
            return
        try:
            t = self.current_triangle
            self.preview = Triangle(t[0], t[1], t[2], angle=self.current_angle, offset=event.pos(), tt=self.current_selection)
        except BaseException as e:
            print('error:', e)
            return
        self.repaint()

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        if self.current_angle is None:
            return
        try:
            t = self.current_triangle
            self.triangles.append(Triangle(t[0], t[1], t[2], angle=self.current_angle, offset=event.pos(), tt=self.current_selection))
        except BaseException as e:
            print('error:', e)
            return
        self.repaint()