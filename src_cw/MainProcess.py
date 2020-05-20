import time, json
from typing import List, Dict
from random import choice

from src_cw.TimeModel import TimeModel
from src_cw.Stock import Stock
from src_cw.Worker import Worker
from src_cw.Worker import WorkerStatus as ws
from src_cw.Queue import Queue, QueueFull
from src_cw.ConnectionManager import ConnectionManager


class MainProcess():
    def __init__(self, N, T, M, R, workers):
        self.stockmans = [Stock(R) for _ in range(N)]
        self.workers = [Worker(T) for _ in range(workers)]
        self.time_model = TimeModel()
        self.queue = Queue(M)
        self.idle = True
        self.conn = ConnectionManager('127.0.0.1', 5555)
        self.waiting_workers = 0
    
    def setup(self, N, T, M, R, workers):
        self.stockmans = [Stock(R) for _ in range(N)]
        self.workers = [Worker(T) for _ in range(workers)]
        self.time_model = TimeModel()
        self.queue = Queue(M)
        self.idle = True
        self.waiting_workers = 0

    def start(self):
        self.conn.wait_connect()
        while self.idle:
            self.time_model.set_scale(0.001)
            self.waiting_workers = 0
            # input('')


            for stockman in self.stockmans:
                self.queue = stockman.process(self.queue)
            for worker in self.workers:
                worker.react_on_time()
                if worker.status == ws.NEED_UPDATE:
                    try:
                        self.queue.add_worker(worker)
                        worker.set_status(ws.WAITING)
                    except QueueFull:
                        continue
                if worker.status == ws.WAITING:
                    self.waiting_workers += 1
            for worker in self.queue.waiting:
                if worker.status == ws.WAITING:
                    free_stockmans = [i for i, x in enumerate(self.stockmans) if x.is_free]
                    # print('free stockmans:', free_stockmans)
                    if len(free_stockmans) != 0:
                        ch = choice(free_stockmans)
                        self.stockmans[ch].update_worker(id(worker))
                        worker.set_status(ws.UPDATING)
                if worker.status == ws.IDLE:
                    self.queue.remove(worker)
            self.queue.process()
            self.sync_data()
            self.time_model.delay(1)
            print('---- time passed ----')
            # print(self)

    def sync_data(self):
        self.conn.send_to_clients(self.json())
        data = self.conn.recvfrom(0)
        data : Dict = json.loads(data)
        assert 'type' in data.keys()
        if data['type'] == 'break':
            self.idle = False
        if data['type'] == 'continue':
            pass
        if 'settings' in data.keys():
            self.update_settings(data['settings'])

    def update_settings(self, settings: Dict):
        if 'idle' in settings.keys():
            self.idle = settings['idle']
        if 'setup' in settings.keys():
            assert len(settings['setup']) == 5
            N, T, M, R, W = settings['setup']
            self.setup(N, T, M, R, W)
        # pass

    def __str__(self):
        ret = ""
        ret += '----------'
        ret += f"Stockmans: {len(self.stockmans)}\n"
        ret += f"Workers: {len(self.workers)}\n"
        ret += f"Queue: {len(self.queue)}\n"
        ret += f"TimeModel: {self.time_model}\n"
        ret += '----------'
        return ret

    def json(self):
        data = {
            'stockmans': len(self.stockmans),
            'workers': len(self.workers),
            'queue': self.queue.json(),
            'waiting': self.waiting_workers
        }
        return json.dumps(data, ensure_ascii=False)

    # def stop()

if __name__ == "__main__":
    test = MainProcess(1, 10, 20, 3)
    test.start()