from src_03.Polynomial import Polynomial
from src_03.number import number
from src_03.ui.MainDialog import Ui_lab_03 as MainDialog

from PyQt5.QtCore import Qt
from PyQt5.Qt import QMainWindow, QApplication, QDialog
from PyQt5.QtWidgets import QApplication, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui : MainDialog = MainDialog()
        self.ui.setupUi(self)
        self.ui.btn.clicked.connect(self.action)
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
            return
        if e.key() == Qt.Key_Return:
            self.action()
            return
    
    def action(self):
        # self.ui.info.setText("test")
        try:
            l : list = [number(x) for x in self.ui.input.text().strip().split(',')]
        except:
            print('error ecountered:', self.ui.input.text())
            self.ui.info.setText("Невозможно определить полином")
            return
        poly = Polynomial(l)
        self.ui.info.setText(str(poly))
        r = poly.roots()
        plus = " +" if r[0].imag > 0 else " "
        self.ui.one.setText(f"{r[0].real:.3f}{plus}{r[0].imag:.3f}j")
        plus = " +" if r[1].imag > 0 else " "
        self.ui.two.setText(f"{r[1].real:.3f}{plus}{r[1].imag:.3f}j")
        # self.ui.two.setText(str(r[1]))



class MyApp():
    # def __init__(self):
    #     QWidget.__init__(self)
    
    def exec(self) -> int:
        app = QApplication([])
        app.setStyle('Fusion')
        window = MyWindow()
        # flags =
        # window.setWindowFlags(flags)
        # window.setFixedSize(807, 596)

        window.show()
        
        return app.exec()
