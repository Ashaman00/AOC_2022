import pyperclip
from time import process_time
from dataclasses import dataclass

FULL = '⬜'  # '█'
EMPTY = '  '  # '░'


def result(r, n=[1]):
	t = process_time()
	if t < 10:
		print(f'Part {n[0]}: {r} - ({1000*t:.2f} ms)')
	else:
		print(f'Part {n[0]}: {r} - ({t:.2f} s)')
	n[0] += 1
	pyperclip.copy(r)


def fname(day, test=False):
	if test:
		return f'../inputs/test{day}.txt'
	return f'../inputs/day{day}.txt'


##############################################

@dataclass
class Bounds:
	xmin: int
	ymin: int
	xmax: int
	ymax: int


def within(x, y, bounds):
	if bounds is None:
		return True
	return bounds.xmin <= x < bounds.xmax and bounds.ymin <= y < bounds.ymax


def neigh_deltas(x, y, deltas, bounds=None):
	for dx, dy in deltas:
		if within(x+dx, y+dy, bounds):
			yield x+dx, y+dy


def neigh4(x, y, bounds=None):
	yield from neigh_deltas(x, y, ((-1, 0), (1, 0), (0, -1), (0, 1)), bounds)


def neigh8(x, y, bounds=None):
	yield from neigh4(x, y, bounds)
	yield from neigh_deltas(x, y, ((-1, -1), (1, -1), (-1, 1), (1, 1)), bounds)


def neigh9(x, y, bounds=None):
	yield from neigh8(x, y, bounds)
	yield x, y
