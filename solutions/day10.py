import advent

res1 = 0
res2 = '\n'


def one_cycle(cycle, x):
	global res1, res2
	if cycle % 40 == 20:
		res1 += (cycle) * x

	res2 += advent.FULL if abs(x - (cycle - 1) % 40) <= 1 else advent.EMPTY
	if cycle % 40 == 0:
		res2 += '\n'

#################################################


with open(advent.fname(10)) as f:
	instrs = [l.strip() for l in f.readlines() if l != '']

cycle, x = 1, 1
one_cycle(cycle, x)

for inst in instrs:
	cycle += 1
	one_cycle(cycle, x)
	if inst != 'noop':
		cycle += 1
		x += int(inst.split()[1])
		one_cycle(cycle, x)

advent.result(res1)
advent.result(res2)
