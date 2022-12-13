import advent
from itertools import zip_longest
from functools import cmp_to_key

SMALLER = -1
EQUAL = 0
BIGGER = 1


def parse(lines):
	p1, p2 = lines.split('\n')
	return eval(p1), eval(p2)


def compare(l1, l2):
	if isinstance(l1, int) and isinstance(l2, int):
		return SMALLER if l1 < l2 else (BIGGER if l1 > l2 else EQUAL)
	if isinstance(l1, int):
		return compare([l1], l2)
	if isinstance(l2, int):
		return compare(l1, [l2])

	for x, y in zip_longest(l1, l2):
		if x is None:
			return SMALLER
		if y is None:
			return BIGGER
		comp = compare(x, y)
		if comp != EQUAL:
			return comp
	return EQUAL


#################################################

with open(advent.fname(13)) as f:
	pairs = [parse(l) for l in f.read()[:-1].split('\n\n')]

res1 = sum(i+1 for i, p in enumerate(pairs) if compare(*p) == SMALLER)
advent.result(res1)


div1, div2 = [[2]], [[6]]
full = [p for pair in pairs for p in pair] + [div1, div2]
full.sort(key=cmp_to_key(compare))
advent.result((full.index(div1) + 1) * (full.index(div2) + 1))
