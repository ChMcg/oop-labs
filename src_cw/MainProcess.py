from src_cw.TimeModel import TimeModel
from random import choice

from src_cw.Stock import Stock
from src_cw.Worker import Worker
from src_cw.Worker import WorkerStatus as ws
from src_cw.Queue import Queue, QueueFull



class MainProcess():
    def __init__(self, N, T, M, R):
        self.stockmans = [Stock(R) for _ in range(N)]
        self.workers = [Worker(T) for _ in range(2)]
        self.time_model = TimeModel()
        self.queue = Queue(M)

    def start(self):
        idle = True
        while idle:
            # self.time_model.set_scale(0.001)
            # input('')

            for stockman in self.stockmans:
                self.queue = stockman.process(self.queue)
            for worker in self.workers:
                worker.react_on_time()
                if worker.status == ws.NEED_UPDATE:
                    worker.set_status(ws.WAITING)
                if worker.status == ws.WAITING:
                    free_stockmans = [i for i, x in enumerate(self.stockmans) if x.is_free]
                    # print('free stockmans:', free_stockmans)
                    try:
                        self.queue.add_worker(worker)
                        worker.set_status(ws.WAITING)
                    except QueueFull:
                        continue
                    if len(free_stockmans) != 0:
                        ch = choice(free_stockmans)
                        self.stockmans[ch].update_worker(id(worker))
                        worker.set_status(ws.UPDATING)
                if worker.status == ws.UPDATING:
                    pass
                
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