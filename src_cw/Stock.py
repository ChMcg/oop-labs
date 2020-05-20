from src_cw.Worker import Worker
from src_cw.Worker import WorkerStatus as ws
from src_cw.Queue import Queue
from typing import List


class Stock():
    def __init__(self, R: int):
        self.time_of_work = R
        self.is_free = True
        self.time_left = 0
        self.pending_worker_id = None

    def update_worker(self, worker_id: Worker):
        # print(self, 'start serving worker', worker_id)
        self.pending_worker_id = worker_id
        self.time_left = self.time_of_work
        self.is_free = False
    
    def process(self, queue: Queue) -> Queue:
        # print(queue.waiting)
        for i, worker in enumerate(queue.waiting):
            # print(self.pending_worker_id, id(worker))
            if self.pending_worker_id == id(worker):
                self.time_left -= 1
                if self.time_left <= 0:
                    queue.waiting[i].update()
                    # queue.remove(queue.waiting[i])
                    queue.waiting[i].set_status(ws.IDLE)
                    self.is_free = True
                    # print(self, 'now free')
                    # queue.waiting[i].update()
                    # queue.waiting.remove(queue[i])
                    break
        return queue
        # for i, worker in enumerate(queue):
        #     if self.pending_worker_id == id(worker):
        #         self.time_left -= 1
        #         if self.time_left <= 0:
        #             queue[i].update()
        #             self.is_free = True
        #             queue.remove(queue[i])
        #         return queue
                
                    

# if __name__ == "__main__":
#     pass

