from cmath import sqrt as _sqrt

# from math import sqrt as s

def sqrt(obj):
    if isinstance(obj, Complex):
        pass
    elif obj < 0:
        pass
    else:
        return _sqrt(obj)


class Complex():
    def __init__(self, x: float, y: float = 0):
        self.value = (x, y)
    
    
    # def sqrt(self):

    