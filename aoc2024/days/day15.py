from typing import List
from ..util import *
import matplotlib.pyplot as plt


def get_next_coord(coord: tuple[int], dir: str):
    x, y = coord
    match dir:
        case "^": y -= 1
        case "v": y += 1
        case ">": x += 1
        case "<": x -= 1
    return (x, y)

def move(coord: tuple[int], dir: str, map: dict):
    next_coord = get_next_coord(coord, dir)
    next_item = map[next_coord]
    if next_item == "#":
        return False
    if next_item == "O":
        if not move(next_coord, dir, map):
            return False
    map[coord], map[next_coord] = map[next_coord], map[coord]
    return next_coord

def print_map(maps: dict): #for testing
    temp_x, temp_y = map(max, zip(*maps))
    res = [[maps.get((i, j), 0) for i in range(temp_y + 1)] for j in range(temp_x + 1)]
    print(*["".join(r) for r in res], sep="\n")

def execute(data: List[str], test_data: List[str]):
    # data = test_data
    data_break = data.index("")
    
    maps = dict()
    for y, d in enumerate(data[:data_break]):
        for x, v in enumerate(d):
            maps[(x, y)] = v

    for k, v in maps.items():
        if v == "@":
            robot_coord = k
            break

    move_list = data[data_break+1:]

    for moves in move_list:
        for m in moves:
            robot_coord = move(robot_coord, m, maps) or robot_coord

    coord_sum = 0
    for k, v in maps.items():
        if v == "O":
            coord_sum += k[0] + k[1]*100

    r2 = 2
    return coord_sum, r2
