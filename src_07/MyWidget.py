from PyQt5 import QtCore, QtGui, QtWidgets
# from src_07.Triangle import Triangle, TriangleType
from src_07.Drawable import Drawable, GridType, Circle, Ellipse, Square, Rectangle
from src_07.Drawable import RegularGrid, RandomGrid
from typing import List, Tuple
from enum import Enum
from math import pi


class MyWidget(QtWidgets.QWidget):
    def __init__(self, some):
        super().__init__(some)
        self.setMouseTracking(True)
        self.mainPen = QtGui.QPen(QtGui.QColor(0x0d47a1), 3)
        self.tempPen = QtGui.QPen(QtGui.QColor(0x0d47a1), 1)
        self.gridPen = QtGui.QPen(QtGui.QColor(0xEEEEEE))
        self.brush = QtGui.QBrush(QtGui.QColor(0x0d47a1), QtCore.Qt.BDiagPattern)
        self.objects : List[Drawable] = []
        self.preview : Drawable = None
        self.grid : Drawable = None
        self.repaint()
    
    def paintEvent(self, event: QtGui.QPaintEvent):
        if self.grid is None:
            self.grid : Drawable = RegularGrid([1, 1], self.geometry())
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setPen(self.mainPen)
        # for triangle in self.triangles:
        #     painter.setBrush(QtCore.Qt.cyan)
        #     painter.setPen(QtCore.Qt.darkCyan)
        #     painter.drawPolygon(triangle)
        #     painter.setBrush(QtCore.Qt.NoBrush)
        if self.grid:
            painter.setPen(self.gridPen)
            self.grid.draw(painter)
        for item in self.objects:
            painter.setBrush(self.brush)
            painter.setPen(self.mainPen)
            item.draw(painter)
            painter.setBrush(QtCore.Qt.NoBrush)
        if self.preview:
            painter.setPen(self.tempPen)
            # painter.drawPolygon(self.preview)
            self.preview.draw(painter)
            # painter.drawEllipse()
        painter.end()

    def updateGrid(self, dense_x: int, dense_y: int, grid_type: GridType):
        self.grid = Grid([dense_x, dense_y], self.geometry(), grid_type)
        self.repaint()

    def cleanup(self):
        self.objects.clear()
        self.repaint()

    # def updateSelection(self, selection: TriangleType):
    #     self.current_selection = selection

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        self.preview : Drawable = Circle(100, event.pos())
        self.repaint()

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        # if self.current_angle is None:
        #     return
        # try:
        #     # t = self.current_triangle
        #     # self.triangles.append(Triangle(t[0], t[1], t[2], angle=self.current_angle, offset=event.pos(), tt=self.current_selection))
        # except BaseException as e:
        #     print('error:', e)
        #     return
        self.repaint()