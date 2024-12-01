from typing import List
from ..util import *


def execute(data: List[str]):
    l1 = sorted([int(d.split()[0]) for d in data])
    l2 = sorted([int(d.split()[1]) for d in data])
    r1 = sum([abs(a-b) for a, b in zip(l1, l2)])
    r2 = sum([e * l2.count(e) for e in l1])

    return r1, r2
