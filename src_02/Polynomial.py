from typing import List, Tuple
from functools import reduce
# from cmath import sqrt
from src_03.number import number, sqrt

class Polynomial:
    def __init__(self, vec : List[number]):
        assert isinstance(vec, list)
        assert len(vec) > 0
        self.v = vec
        self.dim = len(vec)

    def __call__(self, x):
        return reduce(lambda x, y: x+y, [ self.v[i]*(x**i) for i in range(self.dim) ], 0)

    def _is_have_roots_d3(self, vec: List[number]):
        assert len(vec) == 3
        a, b, c = vec[::-1]
        h = -b / (2*a)
        if (self(h) > 0 and a > 0) or (self(h) < 0 and a < 0):
            return False
        else:
            return True
        
    def roots(self) -> Tuple[number, number]:
        def _form_roots_square(v : List):
            a, b, c = self.v[::-1]
            return ((-b + sqrt(b**2 - 4*a*c)) / (2*a), 
                    (-b - sqrt(b**2 - 4*a*c)) / (2*a))
            
        if self.dim-1 != 2:
            raise NotImplementedError('only 2-dimensional polynomials implemented')
        else:
            # if self._is_have_roots_d3(self.v):
            return _form_roots_square(self.v)
            # else:
                # raise ValueError('Polynomial doesn\'t have roots')

    def __str__(self):
        ret = ' '.join( [f"+{self.v[i]}*x^{i}" for i in range(self.dim)[::-1]] )
        return ret