import advent
from itertools import takewhile

def visible(i, j, trees):
	h = trees[i][j]
	ni, nj = len(trees), len(trees[0])
	return all(trees[k][j] < h for k in range(i)) \
		or all(trees[i][k] < h for k in range(j)) \
		or all(trees[k][j] < h for k in range(i+1, ni)) \
		or all(trees[i][k] < h for k in range(j+1, nj))


def scenic(i, j, trees):
	h = trees[i][j]
	ni, nj = len(trees), len(trees[0])
	if i == 0 or j == 0 or i == ni-1 or j == nj-1:
		return 0

	left = next(k for k in range(i-1, -1, -1) if k == 0 or trees[k][j] >= h)
	top = next(k for k in range(j-1, -1, -1) if k == 0 or trees[i][k] >= h)
	right = next(k for k in range(i+1, ni) if k == ni-1 or trees[k][j] >= h)
	bot = next(k for k in range(j+1, nj) if k == nj-1 or trees[i][k] >= h)
	return (i-left) * (j-top) * (right-i) * (bot-j)

#################################################

with open(advent.fname(8)) as f:
	trees = [list(map(int, l.strip())) for l in f.readlines() if l != '']

ni, nj = len(trees), len(trees[0])
res1 = sum(1 for i in range(ni) for j in range(nj) if visible(i, j, trees))
advent.result(res1)

res2 = max(scenic(i, j, trees) for i in range(ni) for j in range(nj))
advent.result(res2)
