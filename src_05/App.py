import json, socket, time
from typing import List
from src_05.ui.MainDialog import Ui_lab_03 as MainDialog
from src_05.config import UDP_IP, UDP_PORT
from src_05.Polynomial import Polynomial
from src_05.number import number

from PyQt5.QtCore import Qt
from PyQt5.Qt import QMainWindow, QApplication, QDialog
from PyQt5.QtWidgets import QApplication, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui : MainDialog = MainDialog()
        self.ui.setupUi(self)
        self.ui.btn.clicked.connect(self.action)
        self.ui.input.textEdited.connect(self.validate_poly)
        self.ui.selector.currentIndexChanged.connect(self.validate_poly)
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
            return
        if e.key() == Qt.Key_Return:
            self.action()
    
    def validate_poly(self):
        try:
            v = [x.strip() for x in self.ui.input.text().strip().replace('i','j').split(',')]
            assert len(v) == 3
            self.validate_input(v)
            print('yep:', v)
            self.ui.btn.setEnabled(True)
        except BaseException as e:
            print('err:', v)
            print(e)
            self.ui.btn.setEnabled(False)
            self.ui.info.setText('')

    def validate_input(self, a: List[str]):
        poly_type = self.ui.selector.currentIndex()
        if poly_type == 0:
            poly = Polynomial(a, int)
            self.ui.info.setText(str(poly))
        if poly_type == 1:
            poly = Polynomial(a, complex)
            self.ui.info.setText(str(poly))


    # def validate_input(self, a: List[str]) -> bool:
    #     poly_type = self.ui.selector.currentIndex()
    #     if poly_type == 0:
    #         try:
    #             poly = Polynomial(a, int)
    #             self.ui.info.setText(str(poly))
    #             return True
    #         except BaseException as e:
    #             return False
    #     if poly_type == 1:
    #         try:
    #             poly = Polynomial(a, complex)
    #             self.ui.info.setText(str(poly))
    #             return True
    #         except BaseException as e:
    #             return False

    def action(self):
        l = []
        try:
            l : list = [x.strip() for x in self.ui.input.text().strip().replace('i','j').split(',')]
        except:
            print('error ecountered:', self.ui.input.text())
            self.ui.info.setText("Невозможно определить полином")
            return
        sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
        sock.bind((UDP_IP, UDP_PORT+1))
        # idx = self.ui.selector.currentIndex()
        poly_type = ['int', 'complex'][self.ui.selector.currentIndex()]
        data = {
            'poly': l,
            'type': poly_type
        }
        sock.sendto(json.dumps(data, ensure_ascii=False, indent=2).encode(),
                    (UDP_IP, UDP_PORT))
        data, _ = sock.recvfrom(1024)
        tn = time.strftime('%Y-%m-%d_%H:%M', time.localtime())
        print(f"[{tn}] recieved:\n", data.decode(), sep='')
        ret = json.loads(data.decode())
        self.ui.info.setText(ret['info'])
        self.ui.one.setText(ret['roots'][0])
        self.ui.two.setText(ret['roots'][1])




class MyApp():
    def exec(self) -> int:
        app = QApplication([])
        app.setStyle('Fusion')
        window = MyWindow()
        window.show()
        return app.exec()
