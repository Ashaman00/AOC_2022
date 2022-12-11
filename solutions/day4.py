import advent


def read_pair(line):
	p1, p2 = line.strip().split(',')
	p1 = [int(n) for n in p1.split('-')]
	p2 = [int(n) for n in p2.split('-')]
	return p1, p2


def contains(p1, p2):
	return p1[0] <= p2[0] and p2[1] <= p1[1]


def overlap(p1, p2):
	if p1[0] > p2[0]:
		return p2[1] >= p1[0]
	return p1[1] >= p2[0]

#################################################


with open(advent.fname(4)) as f:
	lines = [read_pair(l) for l in f.readlines()]

tot1, tot2 = 0, 0
for p1, p2 in lines:
	if contains(p1, p2) or contains(p2, p1):
		tot1 += 1
	if overlap(p1, p2):
		tot2 += 1

advent.result(tot1)
advent.result(tot2)
