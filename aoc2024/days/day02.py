from typing import List
from ..util import *
import itertools



def execute(data: List[str]):
    def check(d: List[int]):
        trend = (d[1] - d[0]) > 0
        for a, b in itertools.pairwise(d):
            ab = a-b
            if not 1 <= abs(ab) <= 3 or bool(ab>0) == trend:
                return False
        return True
    
    def upd_check(d: List[int]):
        for i in range(len(d)):
            dd = d[:]
            dd.pop(i)
            if check(dd): return True
        return False

    data = [list(map(int, d.split())) for d in data]
    r1 = len(list(filter(check, data)))
    r2 = len(list(filter(upd_check, data)))
    return r1, r2
