from typing import List
from ..util import *
from collections import defaultdict

def get_neighbour_coords(x, y):
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)


def execute(data: List[str], test_data: List[str]):
    def create_path():
        for x, d in enumerate(data):
            if (y := d.find("S")) >= 0:
                start = (x, y)

        path = [start]
        prev_node = (0,0)
        while True:
            next_node = return_next(*path[-1], *prev_node)
            if len(next_node) == 0:
                break
            prev_node = path[-1]
            path.append(next_node[0])
        return path

    def coord_on_map(x, y):
        return (0 <= x < len(data)) and (0 <= y < len(data))
    
    def get_data_val(x, y):
        return data[x][y] if coord_on_map(x, y) else "#"

    def check_next(nx, ny, px, py):
        return get_data_val(nx, ny) in [".", "E"] and (nx, ny) != (px, py)

    def return_next(x, y, px, py):
        return [next_coord for next_coord in get_neighbour_coords(x, y) if check_next(*next_coord, px, py)]
    
    def get_cheat_opts(x, y):
        walls = [next_coord for next_coord in get_neighbour_coords(x, y) if get_data_val(*next_coord) == "#"]
        track_points = []
        for wall in walls:
            for t in get_neighbour_coords(*wall):
                if check_next(*t, x, y):
                    track_points.append((wall, t))
        return track_points

    track_path = create_path()

    cheats = defaultdict(list)
    for index, node in enumerate(track_path):
        cheat_opts = get_cheat_opts(*node)
        for opt in cheat_opts:
            if opt[1] in track_path:
                opt_ind = track_path.index(opt[1])
                saved_time = opt_ind - index - 2
                if saved_time > 0:
                    cheats[saved_time].append(opt)

    fast_cheats = {k: v for k, v in cheats.items() if k >= 100}
    r1 = sum([len(v) for v in fast_cheats.values()])
    r2 = 2


    return r1, r2
