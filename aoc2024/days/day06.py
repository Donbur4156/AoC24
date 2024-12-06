from typing import List
from ..util import *


def execute(data: List[str]):
    def operators():
        while True:
            yield (-1, 0)
            yield (0, 1)
            yield (1, 0)
            yield (0, -1)

    def next_position(pos, op):
        return (pos[0] + op[0], pos[1] + op[1])
    
    def pos_in_field(pos):
        return (0 <= pos[0] < 130) and (0 <= pos[1] < 130)
    
    def hit_obstacle(field, x, y):
        return field[x][y] in ("#", "O")
    
    def add_obstacle(field, x, y):
        row = field[x]
        row = row[:y] + "O" + row[y + 1:]
        field[x] = row
        return field

    for e, d in enumerate(data):
        if (p := d.find("^")) > 0:
            start_pos = (e, p)
    
    pos_visited: set[tuple[int]] = {start_pos}

    ops = operators()
    op = next(ops)
    pos = start_pos
    while True:
        next_pos = next_position(pos, op)
        if not pos_in_field(next_pos):
            break
        if hit_obstacle(data, *next_pos):
            op = next(ops)
        else:
            pos = next_pos
            pos_visited.add(pos)
    
    r1 = len(pos_visited)

    obst_pos_possibles = pos_visited.copy()
    obst_pos_possibles.remove(start_pos)
    obst_options: set = set()

    for obst_pos in obst_pos_possibles:
        field_obs = data.copy()
        field_obs = add_obstacle(field_obs, *obst_pos)
        ops = operators()
        op = next(ops)
        pos = start_pos
        waypoints: set[tuple] = {(start_pos, op)}
        while True:
            next_pos = next_position(pos, op)
            if not pos_in_field(next_pos):
                break
            if (next_pos, op) in waypoints:
                obst_options.add(obst_pos)
                break
            if hit_obstacle(field_obs, *next_pos):
                op = next(ops)
            else:
                pos = next_pos
                waypoints.add((pos, op))

    r2 = len(obst_options)
    return r1, r2
