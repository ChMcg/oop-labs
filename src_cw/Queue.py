
from typing import List
from src_cw.Worker import Worker

class QueueFull(Exception):
    pass

class Queue():
    def __init__(self, M):
        self.waiting : List[Worker] = []
        self.limit = M

    def add_worker(self, worker: Worker):
        if len(self.waiting) >= self.limit:
            raise QueueFull
        if not worker in self.waiting: 
            self.waiting.append(worker)
            print(worker, 'added to queue')
    
    def is_already_waiting(self, worker):
        return worker in self.waiting
    
    def remove(self, worker):
        self.waiting.remove(worker)
    
    def process(self):
        for worker in self.waiting:
            if not worker.is_need_update:
                self.waiting.remove(worker)
    
    def __len__(self):
        return len(self.waiting)

