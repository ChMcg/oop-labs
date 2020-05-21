#!/bin/env python3
from enum import Enum
from random import randint

class WorkerStatus(Enum):
    IDLE = 0
    NEED_UPDATE = 1
    UPDATING = 2
    WAITING = 3

class Worker():
    def __init__(self, T: int):
        self.period = T + randint(0-T//3, T//3)
        self.time_left = T
        self.is_need_update = False
        self.status = WorkerStatus.IDLE

    def react_on_time(self):
        self.time_left -= 1
        if self.time_left <= 0 and self.status == WorkerStatus.IDLE:
            self.is_need_update = True
            self.status = WorkerStatus.NEED_UPDATE
            # print(self, 'need update')
        print(self, self.status)          
    
    def update(self):
        # self.is_need_update = False
        self.status = WorkerStatus.IDLE
        self.time_left = self.period
        # print(self, 'updated')
    
    def set_status(self, status: WorkerStatus):
        self.status = status

    def work(self):
        pass #)


if __name__ == "__main__":
    a = Worker(10)
    b = Worker(20)
    c = [a, b]
    print(a in c)
    print(id(a))
