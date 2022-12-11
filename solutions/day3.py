import advent


def value(char):
	c = ord(char)
	if ord('a') <= c <= ord('z'):
		return c - ord('a') + 1
	return c - ord('A') + 27


def find_common(line):
	n = len(line)//2
	s = set(line[:n]).intersection(set(line[n:]))
	return value(s.pop())


def all_three(l1, l2, l3):
	s = set(l1)
	s = s.intersection(set(l2))
	s = s.intersection(set(l3))
	return value(s.pop())

#################################################


with open(advent.fname(3)) as f:
	lines = [l.strip() for l in f.readlines()]

tot1 = sum(find_common(l) for l in lines)
advent.result(tot1)

tot2 = 0
for i in range(0, len(lines)-1, 3):
	tot2 += all_three(lines[i], lines[i+1], lines[i+2])
advent.result(tot2)
