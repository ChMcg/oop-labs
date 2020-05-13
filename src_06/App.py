import json, socket, time
from typing import List
from src_06.ui.lab_6_ui import Ui_Form as MainDialog
from src_06.MyWidget import MyWidget
from src_06.Triangle import TriangleType

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
        self.pen = QPen(QColor(250, 0, 0))
        self.pen.setWidth(2)
        self.brush = QBrush(QColor(250, 20, 20))
        # ---- radio buttons selection ----
        self.ui.radioButton.clicked.connect(self.update_TT)
        self.ui.radioButton_2.clicked.connect(self.update_TT)
        self.ui.radioButton_3.clicked.connect(self.update_TT)
        # ---- clean button ----
        self.ui.clean.clicked.connect(self.cleanup)
        # ---- triangle parameters updated ----
        self.ui.line_a.valueChanged.connect(self.update_triangle)
        self.ui.line_b.valueChanged.connect(self.update_triangle)
        self.ui.line_c.valueChanged.connect(self.update_triangle)
        self.ui.angle.valueChanged.connect(self.update_triangle)
        
    
    def setup_custom_classes(self):
        self.ui.widget = MyWidget(self)
        self.ui.widget.setGeometry(QRect(20, 20, 481, 521))
            
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
            return
        if e.key() == Qt.Key_Return:
            self.action()

    def update_TT(self):
        print('updating TT:', end=" ")
        if self.ui.radioButton.isChecked():
            print('TriangleType.RIGHT')
            self.ui.widget.updateSelection(TriangleType.RIGHT)
            self.ui.line_c.setEnabled(False)
            self.ui.angle.setEnabled(False)
        if self.ui.radioButton_2.isChecked():
            print('TriangleType.ISOSCELES')
            self.ui.widget.updateSelection(TriangleType.ISOSCELES)
            self.ui.line_b.setEnabled(False)
            self.ui.line_c.setEnabled(False)
            self.ui.angle.setEnabled(True)
        if self.ui.radioButton_3.isChecked():
            print('TriangleType.EQUILATERAL')
            self.ui.widget.updateSelection(TriangleType.EQUILATERAL)
            self.ui.line_b.setEnabled(False)
            self.ui.line_c.setEnabled(False)
            self.ui.angle.setValue(60)
            self.ui.angle.setEnabled(False)

    def update_triangle(self):
        # self.widget = MyWidget()
        new = (
            int(self.ui.line_a.text()),
            int(self.ui.line_b.text()),
            int(self.ui.line_c.text())
        )
        angle = int(self.ui.angle.text())
        self.ui.widget.update_current_triangle(new, angle)

    def cleanup(self):
        print('cleaning')
        self.ui.widget.cleanup()

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
