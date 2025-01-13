from typing import List
from ..util import *
from collections import defaultdict
from itertools import combinations

def execute(data: List[str], test_data: List[str]):
    def bron_kerbosch(R: set, P: set, X: set):
        if len(P) == 0 and len(X) == 0:
            if len(R) > 2:
                C.append(R)
            return
        
        for v in list(P):
            bron_kerbosch(R.union({v}), P.intersection(cc[v]), X.intersection(cc[v]))
            P.remove(v)
            X.add(v)
    
    # data = test_data

    cc = defaultdict(set)
    for d in data:
        a, b = d.split("-")
        cc[a].add(b)
        cc[b].add(a)

    C = []
    bron_kerbosch(set(), set(cc.keys()), set())

    connection_sets = set()
    for c in C:
        for comb in combinations(c, 3):
            connection_sets.add(tuple(sorted(comb)))

    r1 = len(list(filter(lambda con: any(x.startswith("t") for x in con), connection_sets)))
    r2 = ",".join(sorted(max(C, key=len)))

    return r1, r2
