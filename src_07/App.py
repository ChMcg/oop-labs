import json, socket, time
from typing import List
from src_07.ui.lab_7_ui import Ui_Form as MainDialog
from src_07.MyWidget import MyWidget
from src_07.Drawable import GridType

from PyQt5.QtCore import Qt
from PyQt5.Qt import QMainWindow, QApplication, QDialog, QObject, QEvent
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt5.QtGui import QPolygonF, QPen, QColor, QBrush, QPainter, QFont, QPaintEvent
from PyQt5.QtCore import QPointF, QRect


class MainDialog_mock(MainDialog):
    def __init__(self):
        super().__init__()
        # self.old_setupUi = self.setupUi
    
    def setupUi(self, Form):
        # self.old_setupUi(Form)
        super().setupUi(Form)
        self.widget = MyWidget(self)
        self.widget.setGeometry(QRect(20, 20, 481, 521))
        self.widget.setObjectName("widget")




class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = MainDialog()
        self.ui.setupUi(self)
        self.setup_custom_classes()
        # ---- grid selection ----
        self.ui.random.clicked.connect(self.updateGrid)
        self.ui.random.clicked.connect(self.updateGridSelection)
        self.ui.regular.clicked.connect(self.updateGrid)
        self.ui.regular.clicked.connect(self.updateGridSelection)
        # ---- clean button ----
        self.ui.clean.clicked.connect(self.cleanup)
        # ---- update grid button ----
        self.ui.generate_new.clicked.connect(self.updateGrid)
        # ---- grid parameters updated ----
        self.ui.dense_x.valueChanged.connect(self.updateGrid)
        self.ui.dense_x.valueChanged.connect(self.balanceByX)
        self.ui.dense_y.valueChanged.connect(self.updateGrid)
        self.ui.dense_y.valueChanged.connect(self.balanceByY)
        
    
    def setup_custom_classes(self):
        self.widget = MyWidget(self)
        # self.widget.setGeometry(QRect(10, 30, 500, 500))
        self.widget.setGeometry(QRect(11, 31, 498, 498))
            
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
            return
        if e.key() == Qt.Key_Return:
            self.action()

    def balanceByX(self):
        if self.ui.balance.isChecked():
            self.ui.dense_y.setValue(self.ui.dense_x.value())

    def balanceByY(self):
        if self.ui.balance.isChecked():
            self.ui.dense_x.setValue(self.ui.dense_y.value())

    def updateGrid(self):
        x = int(self.ui.dense_x.value())
        y = int(self.ui.dense_y.value())
        if self.ui.regular.isChecked():
            self.widget.updateGrid(x, y, GridType.REGULAR)
            self.ui.info.setText(f"current grid: ({x}, {y}) [{GridType.REGULAR}]")
        elif self.ui.random.isChecked():
            self.widget.updateGrid(x, y, GridType.RANDOM)
            self.ui.info.setText(f"current grid: ({x}, {y}) [{GridType.RANDOM}]")

    def updateGridSelection(self):
        if self.ui.regular.isChecked():
            self.ui.generate_new.setEnabled(False)
        else:
            self.ui.generate_new.setEnabled(True)

    def updateParameters(self):
        pass

    # def update_TT(self):
    #     print('updating TT:', end=" ")
    #     if self.ui.radioButton.isChecked():
    #         print('TriangleType.RIGHT')
    #         self.ui.widget.updateSelection(TriangleType.RIGHT)
    #         self.ui.line_c.setEnabled(False)
    #         self.ui.angle.setEnabled(False)
    #     if self.ui.radioButton_2.isChecked():
    #         print('TriangleType.ISOSCELES')
    #         self.ui.widget.updateSelection(TriangleType.ISOSCELES)
    #         self.ui.line_b.setEnabled(False)
    #         self.ui.line_c.setEnabled(False)
    #         self.ui.angle.setEnabled(True)
    #     if self.ui.radioButton_3.isChecked():
    #         print('TriangleType.EQUILATERAL')
    #         self.ui.widget.updateSelection(TriangleType.EQUILATERAL)
    #         self.ui.line_b.setEnabled(False)
    #         self.ui.line_c.setEnabled(False)
    #         self.ui.angle.setValue(60)
    #         self.ui.angle.setEnabled(False)

    # def update_triangle(self):
    #     # self.widget = MyWidget()
    #     new = (
    #         int(self.ui.line_a.text()),
    #         int(self.ui.line_b.text()),
    #         int(self.ui.line_c.text())
    #     )
    #     angle = int(self.ui.angle.text())
    #     self.ui.widget.update_current_triangle(new, angle)

    def cleanup(self):
        print('cleaning')
        self.widget.cleanup()

    def paintEvent(self, paintEvent : QPaintEvent):
        pass

    def action(self):
        pass


class MyApp():
    def exec(self) -> int:
        app = QApplication([])
        app.setStyle('Fusion')
        window = MyWindow()
        window.show()
        return app.exec()
