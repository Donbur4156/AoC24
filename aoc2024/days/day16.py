from typing import List
from ..util import *
import math
from collections import defaultdict

class NestedDefaultDict(defaultdict):
    def __init__(self, *args, **kwargs):
        super(NestedDefaultDict, self).__init__(NestedDefaultDict, *args, **kwargs)

    def __repr__(self):
        return repr(dict(self))
    
    
def get_next_node(pos, dir, data):
    x, y = pos
    match dir:
        case "n": y -= 1
        case "s": y += 1
        case "e": x += 1
        case "w": x -= 1
    return False if data[y][x] == "#" else (x, y, dir)

def get_rotation(start_dir):
    match start_dir:
        case "n" | "s": return "e", "w"
        case "e" | "w": return "n", "s"

def execute(data: List[str], test_data: List[str]):
    def found_next(next, value):
        cur_val = discovered_positions.get(next[:2], {"a": 0}).get(next[2], {"value": math.inf})
        if value < cur_val.get("value"):
            discovered_positions[next[:2]][next[2]]["value"] = value
            prev_nodes = discovered_positions[next[:2]][next[2]].get("prev_nodes", [])
            prev_nodes.append(node)
            prev_nodes = discovered_positions[next[:2]][next[2]]["prev_nodes"] = prev_nodes
            queue.add(next)
    #data = test_data

    for y, d in enumerate(data):
        if (x := d.find("S")) > 0:
            start = (x, y, "e")
            break
    
    discovered_positions = NestedDefaultDict()
    discovered_positions[start[:2]][start[2]]["value"] = 0
    discovered_positions[start[:2]][start[2]]["prev_nodes"] = []
    queue = {start}
    while queue:
        node = queue.pop()
        dir = node[2]
        pos = node[:2]
        node_val = discovered_positions.get(pos, {"a": 0}).get(dir, {}).get("value", 0)
        next_fwd = get_next_node(pos, dir, data)
        next_rot_dir = get_rotation(dir)
        next_rot_a, next_rot_b = [get_next_node(pos, dir, data) for dir in next_rot_dir]
        if next_fwd:
            found_next(next_fwd, node_val + 1)
        if next_rot_a:
            found_next(next_rot_a, node_val + 1001)
        if next_rot_b:
            found_next(next_rot_b, node_val + 1001)

    for y, d in enumerate(data):
        if (x := d.find("E")) > 0:
            end = (x, y)
            break

    best_path_points = set()
    nodes_checked = set()
    queue = {(*end, "e")}
    while queue:
        node = queue.pop()
        best_path_points.add(node[:2])
        if node[:2] == start[:2]:
            continue
        prev = discovered_positions.get(node[:2], {})
        for v in prev.values():
            prev_nodes = v.get("prev_nodes")
            for n in prev_nodes:
                if not n in nodes_checked:
                    queue.add(n)
                    nodes_checked.add(n)

    r1 = min(x.get("value") for x in discovered_positions.get(end).values())
    r2 = len(best_path_points)


    return r1, r2
