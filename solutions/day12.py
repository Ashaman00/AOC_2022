import advent


def height(pt, hmap):
	h = hmap[pt[0]][pt[1]]
	match h:
		case 'S': return 0
		case 'E': return 25
	return ord(h) - ord('a')


def can_move(orig, dest, hmap, rev=False):
	if rev:
		return height(orig, hmap) <= height(dest, hmap) + 1
	return height(dest, hmap) <= height(orig, hmap) + 1


def find_start(hmap, char):
	for sx, line in enumerate(hmap):
		sy = line.find(char)
		if sy != -1:
			return sx, sy


def shortest(hmap, startc, endc, rev=False):
	st = find_start(hmap, startc)
	vis = {st}
	to_vis = [(0, *st)]
	bounds = advent.Bounds(0, 0, len(hmap), len(hmap[0]))

	while len(to_vis) > 0:
		steps, cx, cy = to_vis.pop(0)
		if hmap[cx][cy] == endc:
			return steps
		for neigh in advent.neigh4(cx, cy, bounds):
			if neigh not in vis and can_move((cx, cy), neigh, hmap, rev):
				vis.add(neigh)
				to_vis.append((steps+1, *neigh))


#################################################

with open(advent.fname(12, test=False)) as f:
	hmap = [l.strip() for l in f.readlines() if l != '']

advent.result(shortest(hmap, 'S', 'E'))
advent.result(shortest(hmap, 'E', 'a', True))
