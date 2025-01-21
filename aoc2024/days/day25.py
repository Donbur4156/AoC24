from typing import List
from ..util import *

def parse_data(data: List[str]):
    locks = list()
    keys = list()
    for scheme in zip(*[iter(data)]*8):
        scheme = scheme[:7]
        if scheme[0] == "#####":
            keys.append([h.count("#") for h in list(zip(*scheme[1:]))])
        else:
            locks.append([h.count("#") for h in list(zip(*scheme[:6]))])
    return locks, keys
                    
def check_key_lock(key, lock):
    summing = list(map(sum, list(zip(key, lock))))
    return all(x<=5 for x in summing)

def execute(data: List[str], test_data: List[str]):
    locks, keys = parse_data(data)
    pair_count = 0
    for lock in locks:
        for key in keys:
            if check_key_lock(key, lock):
                pair_count += 1

    r1 = pair_count
    r2 = 2


    return r1, r2
