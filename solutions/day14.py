import advent
from collections import defaultdict
from itertools import pairwise

AIR = 0
WALL = 1
SAND = 2


def segment(x1, y1, x2, y2):
    if x1 == x2:
        return ((x1, y) for y in range(min(y1, y2), max(y1, y2)+1))
    return ((x, y1) for x in range(min(x1, x2), max(x1, x2)+1))


def sand_in_void(grid, void, x=500, y=0):
    if y >= void:
        return True

    if grid[(x, y + 1)] == AIR:
        return sand_in_void(grid, void, x, y + 1)
    if grid[(x - 1, y + 1)] == AIR:
        return sand_in_void(grid, void, x - 1, y + 1)
    if grid[(x + 1, y + 1)] == AIR:
        return sand_in_void(grid, void, x + 1, y + 1)

    grid[(x, y)] = SAND
    return False


def count_grains(grid, floor, x=500, y=0):
    vis = {(x, y)}
    to_vis = [(x, y)]
    res = 0
    while len(to_vis) > 0:
        x, y = to_vis.pop(0)
        if y == floor or grid[(x, y)] == WALL:
            continue
        res += 1
        for nx in [x, x-1, x+1]:
            if (nx, y+1) not in vis:
                vis.add((nx, y+1))
                to_vis.append((nx, y+1))
    return res


def draw_grid(grid, bds):
    for y in range(bds.ymin, bds.ymax):
        for x in range(bds.xmin, bds.xmax):
            print(' #o'[grid[(x, y)]], end='')
        print()


#################################################

grid = defaultdict(lambda: AIR)
floor = 0
with open(advent.fname(14, test=False)) as f:
    for line in f:
        points = [advent.lmi(p.split(',')) for p in line.split(' -> ')]
        for p1, p2 in pairwise(points):
            for p in segment(*p1, *p2):
                grid[p] = WALL
                floor = max(floor, p[1] + 2)

nsands = 0
while not sand_in_void(grid, floor):
    nsands += 1
advent.result(nsands)
# draw_grid(grid, advent.Bounds(450, 0, 550, floor))
advent.result(count_grains(grid, floor))
