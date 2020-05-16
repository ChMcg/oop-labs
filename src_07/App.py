from src_07.ui.lab_7_ui import Ui_Form as MainDialog
from src_07.MyWidget import MyWidget
from src_07.Drawable import GridType, DrawableType

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QRect


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
        # ---- figure selection ----
        self.ui.rectangle.clicked.connect(self.updateFugureType)
        self.ui.square.clicked.connect(self.updateFugureType)
        self.ui.circle.clicked.connect(self.updateFugureType)
        self.ui.ellipse.clicked.connect(self.updateFugureType)
        # ---- figure parameters update ----
        self.ui.line_a.valueChanged.connect(self.updateParameters)
        self.ui.line_b.valueChanged.connect(self.updateParameters)
        self.ui.radius.valueChanged.connect(self.updateParameters)
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
        # ---- update initial settings ----
        self.updateFugureType()
        self.updateParameters()
        self.updateGridSelection()
        self.updateGrid()
        # ---- custom signals ----
        self.widget.objectAdded.connect(self.updateInfo)
        
    
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
            self.updateInfo()
        elif self.ui.random.isChecked():
            self.widget.updateGrid(x, y, GridType.RANDOM)
            self.updateInfo()
    
    def updateInfo(self):
        x = int(self.ui.dense_x.value())
        y = int(self.ui.dense_y.value())
        info = self.widget.getIntersectResult()
        current, total = info
        gt = self.widget.getGridType()
        self.ui.info.setText(f"Сетка: ({x}, {y}) [{gt}]\n"
                             f"Заплнено: {current}/{total} ({(1-current/total)*100:.2f})")

    def updateGridSelection(self):
        if self.ui.regular.isChecked():
            self.ui.generate_new.setEnabled(False)
        else:
            self.ui.generate_new.setEnabled(True)

    def updateParameters(self):
        self.widget.setCurrentParameters(
            a=self.ui.line_a.value(),
            b=self.ui.line_b.value(),
            radius=self.ui.radius.value()
        )

    def updateFugureType(self):
        if self.ui.rectangle.isChecked():
            self.widget.setCurrentFigure(DrawableType.RECTANGLE)
            self.ui.line_a.setEnabled(True)
            self.ui.line_b.setEnabled(True)
            self.ui.radius.setEnabled(False)
        if self.ui.square.isChecked():
            self.widget.setCurrentFigure(DrawableType.SQUARE)
            self.ui.line_a.setEnabled(True)
            self.ui.line_b.setEnabled(False)
            self.ui.radius.setEnabled(False)
        if self.ui.circle.isChecked():
            self.widget.setCurrentFigure(DrawableType.CIRCLE)
            self.ui.line_a.setEnabled(False)
            self.ui.line_b.setEnabled(False)
            self.ui.radius.setEnabled(True)
        if self.ui.ellipse.isChecked():
            self.widget.setCurrentFigure(DrawableType.ELLIPSE)
            self.ui.line_a.setEnabled(True)
            self.ui.line_b.setEnabled(True)
            self.ui.radius.setEnabled(False)

    def cleanup(self):
        print('cleaning')
        self.widget.cleanup()


class MyApp():
    def exec(self) -> int:
        app = QApplication([])
        app.setStyle('Fusion')
        window = MyWindow()
        window.show()
        return app.exec()
