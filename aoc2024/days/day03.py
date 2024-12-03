from typing import List
from ..util import *
import re


def execute(data: List[str]):
    def calc_mul(mul: str):
        m = list(map(int, re.findall(r"\d{1,3}", mul)))
        return m[0]*m[1]
    
    r1 = 0
    for d in data:
        x = re.findall(r"mul\(\d{1,3},\d{1,3}\)", d)
        r1 += sum(map(calc_mul, x))

    r2 = 0
    enabled = True
    for d in data:
        x = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", d)
        for y in x:
            match y:
                case "do()": enabled = True
                case "don't()": enabled = False
                case _: if enabled: r2 += calc_mul(y) 

    return r1, r2
