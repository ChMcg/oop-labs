import json, socket, time
from src_04.ui.MainDialog import Ui_lab_03 as MainDialog
from src_04.config import UDP_IP, UDP_PORT

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
        data = {
            'poly': l,
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
