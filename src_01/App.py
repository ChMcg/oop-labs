from src_01.Polynomial import Polynomial
from src_01.number import number

class MyApp():
    def exec(self) -> int:
        ch = int()
        while True:
            try:
                ch = int(input('Chose 1: >> '))
            except:
                print('Only numbers accepted')
                continue
            if ch == 1:
                try:
                    l : list = [number(x) for x in input('Enter indexes: >> ').strip().split(',')]
                except:
                    print('error ecountered')
                    continue
                poly = Polynomial(l)
                print('Poly:', poly)
                print('Roots: ', poly.roots())
            elif ch == 0:
                break
            else:
                continue
        print('Exited')
        return 0
