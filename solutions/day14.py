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


def with_floor(grid, floor, x=500, y=0):
    while True:  # swapped the recursion for a while loop, a bit quicker
        if y == floor - 1:
            grid[(x, y)] = SAND
            return False
        elif grid[(x, y + 1)] == AIR:
            y += 1
        elif grid[(x - 1, y + 1)] == AIR:
            x, y = x - 1, y + 1
        elif grid[(x + 1, y + 1)] == AIR:
            x, y = x + 1, y + 1
        else:
            grid[(x, y)] = SAND
            return x == 500 and y == 0


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
        points = [advent.lmapint(p.split(',')) for p in line.split(' -> ')]
        for p1, p2 in pairwise(points):
            for p in segment(*p1, *p2):
                grid[p] = WALL
                floor = max(floor, p[1] + 2)

nsands = 0
while not sand_in_void(grid, floor):
    nsands += 1
advent.result(nsands)
# draw_grid(grid, advent.Bounds(450, 0, 550, floor))

while not with_floor(grid, floor):
    nsands += 1
advent.result(nsands + 1)
