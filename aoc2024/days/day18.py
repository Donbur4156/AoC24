from typing import List
from ..util import *
from collections import defaultdict
import math

def get_neighbour_coords(x, y):
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)

def find_coord_neighbour(coord, region_coords):
    return [c for c in get_neighbour_coords(*coord) if c in region_coords]

def execute(data: List[str], test_data: List[str]):
    def remove_loc():
        x, y = map(int, data.pop(0).split(","))
        locations.remove((x, y))
        return f"{x},{y}"

    def find_path():
        discovered_locs = defaultdict()
        discovered_locs[start] = 0
        queue = {start}

        while queue:
            loc = queue.pop()
            loc_val = discovered_locs.get(loc)
            neighbours = find_coord_neighbour(loc, locations)
            for n in neighbours:
                cur_val = discovered_locs.get(n, math.inf)
                if (loc_val + 1) < cur_val:
                    discovered_locs[n] = loc_val + 1
                    queue.add(n)
        return discovered_locs.get(end, math.inf)

    locations = [(x, y) for x in range(71) for y in range(71)]
    for _ in range(1024):
        remove_loc()

    start = (0,0)
    end = (70,70)
    r1 = find_path()

    while True:
        last_byte = remove_loc()
        if find_path() == math.inf:
            break

    return r1, last_byte
