from typing import List
from ..util import *
from collections import defaultdict

def blink(stones: dict[int,int]):
    output = defaultdict(int)

    for m, q in stones.items():
        if m == 0:
            output[1] += q
        elif len(str(m)) % 2 == 0:
            mid = len(str(m))//2
            output[int(str(m)[:mid])] += q
            output[int(str(m)[mid:])] += q
        else:
            output[m*2024] += q

    return output    

def execute(data: List[str]):
    stones = {int(x): 1 for x in data[0].split()}

    for i in range(25):
        stones = blink(stones)
    
    r1 = sum(stones.values())

    for i in range(50):
        stones = blink(stones)
        print(i, len(stones))

    r2 = sum(stones.values())

    return r1, r2
