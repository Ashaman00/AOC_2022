import advent

def parse(line):
	d, n = line.strip().split()
	return d, int(n)


def follow(fst, snd):
	x1, x2 = fst
	y1, y2 = snd
	if abs(x1 - y1) <= 1 and abs(x2 - y2) <= 1:
		return snd
	z1 = y1 + 1 if y1 < x1 else (y1 - 1 if y1 > x1 else y1)
	z2 = y2 + 1 if y2 < x2 else (y2 - 1 if y2 > x2 else y2)
	return z1, z2


def move(d, snake):
	hx, hy = snake[0]
	newsnake = []
	match d:
		case "U": newsnake.append((hx - 1, hy))
		case "D": newsnake.append((hx + 1, hy))
		case "L": newsnake.append((hx, hy - 1))
		case "R": newsnake.append((hx, hy + 1))
	for elt in snake[1:]:
		newsnake.append(follow(newsnake[-1], elt))
	return newsnake

#################################################

with open(advent.fname(9)) as f:
	moves = [parse(l) for l in f.readlines() if l != '']

snake = [(0,0) for _ in range(10)]
vis1, vis2 = {(0,0)}, {(0,0)}
for d, n in moves:
	for k in range(n):
		snake = move(d, snake)
		vis1.add(snake[1])
		vis2.add(snake[-1])

advent.result(len(vis1))
advent.result(len(vis2))
