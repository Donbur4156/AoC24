from typing import List
from ..util import *
from collections import defaultdict

def get_neighbour_coords(x, y):
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)

def get_radius_coords(x, y, r):
    for xx in range(-r, r+1):
        xr = r - abs(xx)
        for yy in range(-xr, xr+1):
            yield (x+xx, y+yy, abs(xx) + abs(yy))

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
        return check_coord(nx, ny) and (nx, ny) != (px, py)
    
    def check_coord(nx, ny):
        return get_data_val(nx, ny) in [".", "E"]

    def return_next(x, y, px, py):
        return [next_coord for next_coord in get_neighbour_coords(x, y) if check_next(*next_coord, px, py)]
    
    def get_cheat_opts_x(x, y, max_pico_secs):
        coords_in_rad = get_radius_coords(x, y, max_pico_secs)
        track_points = defaultdict()
        for coord in coords_in_rad:
            xc, yc, dc = coord
            if check_coord(xc, yc) and dc > 0:
                track_points[((x,y),(xc,yc))] = dc
        return track_points

    def get_cheats(max_pico_secs = 2):
        cheats = defaultdict(list)
        for index, node in enumerate(track_path):
            cheat_opts = get_cheat_opts_x(*node, max_pico_secs)
            for opt_coords, opt_dis in cheat_opts.items():
                if opt_coords[1] in track_path:
                    opt_ind = track_path.index(opt_coords[1])
                    saved_time = opt_ind - index - opt_dis
                    if saved_time > 0:
                        cheats[saved_time].append(opt_coords)
        return cheats

    def get_sum_of_best_cheats(cheats: dict, min_pico_secs = 100):
        fast_cheats = {k: v for k, v in cheats.items() if k >= min_pico_secs}
        return sum([len(v) for v in fast_cheats.values()])

    track_path = create_path()

    cheats_2 = get_cheats(2)
    cheats_20 = get_cheats(20)

    r1 = get_sum_of_best_cheats(cheats_2, 100)
    r2 = get_sum_of_best_cheats(cheats_20, 100)

    return r1, r2
