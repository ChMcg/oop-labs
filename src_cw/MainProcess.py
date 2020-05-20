from src_cw.TimeModel import TimeModel
from random import choice

from src_cw.Stock import Stock
from src_cw.Worker import Worker
from src_cw.Worker import WorkerStatus as ws
from src_cw.Queue import Queue, QueueFull



class MainProcess():
    def __init__(self, N, T, M, R, workers):
        self.stockmans = [Stock(R) for _ in range(N)]
        self.workers = [Worker(T) for _ in range(workers)]
        self.time_model = TimeModel()
        self.queue = Queue(M)
        self.idle = True

    def start(self):
        while self.idle:
            self.time_model.set_scale(0.001)

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
            self.time_model.delay(1)
            print('---- time passed ----')
            print(self)

    def __str__(self):
        ret = ""
        ret += '----------'
        ret += f"Stockers: {len(self.stockmans)}\n"
        ret += f"Workers: {len(self.workers)}\n"
        ret += f"Queue: {len(self.queue)}\n"
        ret += f"TimeModel: {self.time_model}\n"
        ret += '----------'
        return ret

    # def stop()

if __name__ == "__main__":
    test = MainProcess(1, 10, 20, 3)
    test.start()