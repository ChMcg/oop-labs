from src_cw.ui.cw_ui import Ui_Form as MainDialog
from src_cw.ConnectionManager import ConnectionManager

from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QRect
from typing import *
import time, json

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np


class Canvas(FigureCanvas):
    def __init__(self, parent = None, size: QRect = QRect(0, 0, 100, 100), dpi = 100):
        my_dpi = 96
        width = size.width()/my_dpi
        height = size.height()/my_dpi
        fig = Figure(figsize=(width, height), dpi=dpi)
        # FigureCanvas.__init__(self, fig)
        super(FigureCanvas, self).__init__(fig)
        self.setParent(parent) #TODO
        ax : List[Axes]  = self.figure.subplots(1, 2)
        self.ax1, self.ax2 = ax
        self.ax1.plot(list(range(40)), [0 for _ in range(40)], 'g')
        self.ax1.set_title('Рабочие в ожидании, %')
        self.ax2.plot(list(range(40)), [0 for _ in range(40)], 'g')
        self.ax2.set_title('Заполненность очереди, %')

    def plot(self, a, b):
        self.ax1.cla()
        self.ax2.cla()
        self.ax1.clear()
        self.ax1.set_title('Рабочие в ожидании, %')
        self.ax2.set_title('Заполненность очереди, %')
        x = np.linspace(0, len(a), len(a))
        self.ax1.plot(x, np.array(a), '#B71C1C')
        x = np.linspace(0, len(b), len(b))
        self.ax2.plot(x, np.array(b), '#B71C1C')
        self.draw()


class Updater(QThread):
    data_synced = pyqtSignal()
    conn = None
    settings = None
    def run(self):
        self.idle = True
        self.data_in : List[str] = []
        while self.idle:
            if self.settings:
                data = {
                    'type': 'continue',
                    'settings': self.settings
                }
                self.data_out = json.dumps(data, ensure_ascii=False)
                self.settings = None
            else:
                self.data_out = '{"type": "continue"}'
            print(self.data_out)
            self.conn.send(self.data_out)
            self.data_in.append(self.conn.recv())
            # print(self.data_in[-1])
            if len(self.data_in) > 40:
                self.data_in.pop(0)
            self.data_synced.emit()
    

class MyWindow(QMainWindow):
    data_syncronized = pyqtSignal()
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = MainDialog()
        self.ui.setupUi(self)
        self.settings_ui_group : List[QWidget] = [
            self.ui.stockmans,
            self.ui.time_of_work,
            self.ui.queue_length,
            self.ui.speed_of_service,
            self.ui.workers,
            self.ui.time_scale
        ]
        self.set_settings_enabled(False)
        self.buttons : List[QWidget] = [
            self.ui.update_settings,
            self.ui.stop,
            self.ui.start
        ]
        self.set_buttons_enabled(False)
        self.ui.info.setText('Подключение: нет')
        self.connection = ConnectionManager()
        self.ui.connect.clicked.connect(self.connect_to_server)
        self.is_connected = False
        self.ui.start.clicked.connect(self.start_updating)
        self.ui.stop.clicked.connect(self.stop_updating)
        self.updater = Updater()
        self.updater.conn = self.connection
        self.updater.data_synced.connect(self.update_output)
        self.plot = Canvas(self.ui.graphicsView, self.ui.graphicsView.geometry(), dpi=96)
        self.ui.time_scale.valueChanged.connect(self.update_time_scale)
        for item in self.settings_ui_group:
            item.valueChanged.connect(self.update_settings)

    def update_settings(self):
        N = self.ui.stockmans.value()
        T = self.ui.time_of_work.value()
        M = self.ui.queue_length.value()
        R = self.ui.speed_of_service.value()
        W = self.ui.workers.value()
        if self.updater.settings:
            self.updater.settings['setup'] = [N, T, M, R, W]
        else:
            self.updater.settings = {
                'setup': [N, T, M, R, W]
            }
        
    def update_time_scale(self):
        ts = 1 / 2**self.ui.time_scale.value()
        if self.updater.settings:
            self.updater.settings['time_scale'] = ts
        else:
            self.updater.settings = {
                'time_scale': ts
            }

    def print_data(self):
        print(self.updater.data_in[-1])

    def update_output(self):
        data = json.loads(self.updater.data_in[-1])
        data_in = [json.loads(x) for x in self.updater.data_in]
        self.ui.queue_bar.setValue(int(data['queue']['current']/data['queue']['limit']*100))
        self.ui.workers_bar.setValue(int(data['waiting']/data['workers']*100))
        a = [int(x['waiting']/x['workers']*100) for x in data_in]
        b = [int(x['queue']['current']/x['queue']['limit']*100) for x in data_in]
        self.plot.plot(a, b)

    def start_updating(self):
        if self.is_connected:
            if not self.updater.isRunning():
                self.updater.start()
            else:
                self.updater.idle = True
                
    def stop_updating(self):
        self.updater.idle = False

    def set_settings_enabled(self, choice: bool):
        for item in self.settings_ui_group:
            item.setEnabled(choice)
    
    def set_buttons_enabled(self, choice: bool):
        for item in self.buttons:
            item.setEnabled(choice)

    def connect_to_server(self):
        try:
            addr = self.ui.addr.text()
            port = int(self.ui.port.text())
            self.connection.connect(addr, port)
            self.set_settings_enabled(True)
            self.set_buttons_enabled(True)
            self.ui.info.setText(f'Подключение: установлено ({addr}, {port})')
            self.is_connected = True
            # self.connection.send('{"idle": "continue"}')
        except:
            self.ui.info.setText('Подключение: не удалось')
    
    def stop(self):
        self.idle = False

    def start(self):
        self.idle = True
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Return and not self.is_connected:
            self.connect_to_server()



class MyApp():
    def exec(self) -> int:
        app = QApplication([])
        app.setStyle('Fusion')
        window = MyWindow()
        window.show()
        return app.exec()
