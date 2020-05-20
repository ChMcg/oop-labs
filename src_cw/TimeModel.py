import time


class TimeModel():
    def __init__(self):
        self.scale = 1

    def set_scale(self, scale: float):
        self.scale = scale
    
    def delay(self, secs: int):
        time.sleep(self.scale*secs)

    def __str__(self):
        ret = ""
        ret += f"[scale: {self.scale}]"
        return ret