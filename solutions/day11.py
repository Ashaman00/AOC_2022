import advent
from dataclasses import dataclass
from copy import deepcopy
from math import lcm


@dataclass
class Monkey:
	items: list[int]
	op: str
	test: int
	targT: int
	targF: int
	ninspected: int = 0


def parse(lines):
	it = list(map(int, lines[1].split(': ')[1].split(', ')))
	arith = lines[2].split('= ')[1]
	op = eval(f'lambda old: {arith}')
	test = int(lines[3].split(' ')[-1])
	true = int(lines[4].split(' ')[-1])
	false = int(lines[5].split(' ')[-1])
	return Monkey(it, op, test, true, false)


def make_round(monkeys, is_part1, maxi=0):
	for monke in monkeys:
		monke.ninspected += len(monke.items)
		while len(monke.items) > 0:
			new = monke.op(monke.items.pop())
			new = new // 3 if is_part1 else new % maxi
			targ = monke.targT if new % monke.test == 0 else monke.targF
			monkeys[targ].items.append(new)


def print_round(rnd, monkeys):
	print(f'Round {r+1}:')
	for n, m in enumerate(monkeys):
		print(f'\tMonkey {n}: {m.items}')


def activity(monkeys):
	act1, act2 = sorted(monkeys, key=lambda m: -m.ninspected)[:2]
	return act1.ninspected * act2.ninspected

#################################################


with open(advent.fname(11, test=False)) as f:
	monkeys = [parse(l.split('\n')) for l in f.read()[:-1].split('\n\n')]
	monkeys2 = deepcopy(monkeys)

for r in range(20):
	make_round(monkeys, True)
	# print_round(r, monkeys)
advent.result(activity(monkeys))


maxi = lcm(*[m.test for m in monkeys2])
for r in range(10000):
	make_round(monkeys2, False, maxi)
advent.result(activity(monkeys2))
