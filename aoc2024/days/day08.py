from typing import List
from ..util import *
from collections import defaultdict
from itertools import combinations
from operator import sub, add


def execute(data: List[str]):
    def check_antinode_in_field(an):
        return (0 <= an[0] < field_size) and (0 <= an[1] < field_size)

    def calc_antinodes(a, b):
        dif = tuple(map(sub, a, b))
        an_a = tuple(map(add, a, dif))
        if check_antinode_in_field(an_a):
            antinodes_wo_res_har.add(an_a)
        while check_antinode_in_field(an_a):
            antinodes_wi_res_har.add(an_a)
            an_a = tuple(map(add, an_a, dif))
        
        an_b = tuple(map(sub, b, dif))
        if check_antinode_in_field(an_b):
            antinodes_wo_res_har.add(an_b)
        while check_antinode_in_field(an_b):
            antinodes_wi_res_har.add(an_b)
            an_b = tuple(map(sub, an_b, dif))

        antinodes_wi_res_har.add(a)
        antinodes_wi_res_har.add(b)
        
    field_size = len(data)

    antennas: dict[str, set] = defaultdict(set)
    for r, d in enumerate(data):
        for c, s in enumerate(d):
            if s != ".":
                antennas[s].add((r, c))

    antinodes_wo_res_har: set = set()
    antinodes_wi_res_har: set = set()
    for a in antennas.values():
        for c in combinations(a, 2):
            calc_antinodes(*c)

    r1 = len(antinodes_wo_res_har)
    r2 = len(antinodes_wi_res_har)


    return r1, r2
