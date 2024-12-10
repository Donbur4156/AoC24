from typing import List
from ..util import *

test_data = [
    "89010123",
    "78121874",
    "87430965",
    "96549874",
    "45678903",
    "32019012",
    "01329801",
    "10456732",
]

def execute(data: List[str]):
    def create_pos(x, y):
        yield (x-1, y)
        yield (x+1, y)
        yield (x, y-1)
        yield (x, y+1)

    def pos_in_field(x, y):
        return (0 <= x < field_size) and (0 <= y < field_size)
    
    def check_next_height(x, y, next_height):
        return int(data[x][y]) == next_height

    def find_trail(pos: tuple, height: int, trailheads: list[tuple]):
        if not pos_in_field(*pos): 
            return None
        
        if not check_next_height(*pos, height):
            return None

        if height == 9:
            trailheads.append(pos)
            return trailheads

        for next_pos in create_pos(*pos):
            find_trail(next_pos, height+1, trailheads)
        return trailheads
    
    field_size = len(data)
    r1 = 0
    r2 = 0

    for a, d in enumerate(data):
        for b, dd in enumerate(d):
            if int(dd) == 0:
                trail_ends = find_trail((a,b), 0, [])
                r1 += len(set(trail_ends))
                r2 += len(trail_ends)

    return r1, r2