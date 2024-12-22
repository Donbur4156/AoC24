from typing import List
from ..util import *
from functools import cache

def execute(data: List[str], test_data: List[str]):
    @cache
    def check_design(design: str) -> bool:
        check_sum = 0
        for i in range(min(len(design), longest_pattern), 0, -1):
            if design[:i] in patterns:
                check_sum += 1 if len(design[i:]) == 0 else check_design(design[i:])
        return check_sum
            
    # data = test_data

    patterns = data[0].split(", ")
    longest_pattern = max(map(len, patterns))
    designs = data[2:]
    possible_designs = []
    combination_count = 0
    for design in designs:
        if checks := check_design(design):
            possible_designs.append(design)
            combination_count += checks


    return len(possible_designs), combination_count
