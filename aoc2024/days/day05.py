from typing import List
from ..util import *
from collections import defaultdict

def execute(data: List[str]):
    def check_updates(upd: list[int]):
        for i, p in enumerate(iterable=upd):
            if rules[p].intersection(upd[:i]):
                return False
        return True
    
    def correct_updates(upd: list[int]):
        while True:
            for i, p in enumerate(iterable=upd):
                upd_inter = rules[p].intersection(upd[:i])
                if upd_inter:
                    min_index = min([upd.index(ui) for ui in upd_inter])
                    upd.remove(p)
                    upd.insert(min_index, p)
                    break
            else:
                return upd

    rules: dict[int,set[int]] = defaultdict(set)
    for d in data[:1176]:
        before, after = d.split(sep="|")
        rules[int(before)].add(int(after))
    
    r1 = 0
    r2 = 0
    for u in data[1177:]:
        ul = list(map(int,u.split(sep=",")))
        if check_updates(ul): 
            r1 += ul[int((len(ul)-1)/2)]
        else:
            uu = correct_updates(ul)
            r2 += uu[int((len(uu)-1)/2)]

    return r1, r2
