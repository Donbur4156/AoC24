from typing import List
from ..util import *
from collections import defaultdict

def get_neighbour_coords(x, y):
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)

def find_coord_neighbour(coord, region_coords):
    return [c for c in get_neighbour_coords(*coord) if c in region_coords]

def find_coords_neighbours(coords, region_coords):
    coords_r = set()
    for coord in coords:
        for c in find_coord_neighbour(coord, region_coords):
            coords_r.add(c)
    return coords_r

def map_region(coords: list[tuple[int, int]]):
    regions = []
    while coords:
        region = []
        coord = coords.pop()
        region.append(coord)
        coords_n = [coord]
        while True:
            coords_n = list(find_coords_neighbours(coords_n, coords))
            if len(coords_n) == 0:
                break
            region.extend(coords_n)
            for c in coords_n:
                coords.remove(c)
        regions.append(region)
    return regions

def create_region_dict(data: List[str]):
    region_dict = defaultdict(list)
    for x, d in enumerate(data):
        for y, l in enumerate(d):
            region_dict[l].append((x, y))
    return region_dict

def calc_perimeter(coords: list[tuple]):
    return sum([4 - len(find_coord_neighbour(c, coords)) for c in coords])



def calc_sides(coords: list[tuple]):
    s = 0
    for c in coords:
        N = ((c[0], c[1]-1) in coords)
        E = ((c[0]+1, c[1]) in coords)
        S = ((c[0], c[1]+1) in coords)
        W = ((c[0]-1, c[1]) in coords)
        NE = ((c[0]+1, c[1]-1) in coords)
        SE = ((c[0]+1, c[1]+1) in coords)
        NW = ((c[0]-1, c[1]-1) in coords)
        SW = ((c[0]-1, c[1]+1) in coords)
        if(not N and not E and not S and not W): s+=4
        if(N and not E and not S and not W): s+=2
        if(E and not S and not W and not N): s+=2
        if(S and not W and not N and not E): s+=2
        if(W and not N and not E and not S): s+=2
        if(S and E and not N and not W): s+=1
        if(S and W and not N and not E): s+=1
        if(N and E and not S and not W): s+=1
        if(N and W and not S and not E): s+=1
        if(E and N and not NE): s+=1
        if(E and S and not SE): s+=1
        if(W and N and not NW): s+=1
        if(W and S and not SW): s+=1
    return s

def execute(data: List[str]):
    region_dict: dict = create_region_dict(data)
    for r, cs in region_dict.items():
        region_dict[r] = map_region(cs)
    
    fence_price_peri = 0
    fence_price_sides = 0
    for l in region_dict.values():
        for cs in l:
            fence_price_peri += len(cs) * calc_perimeter(cs)
            fence_price_sides += len(cs) * calc_sides(cs)


    return fence_price_peri, fence_price_sides
