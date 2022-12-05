import advent

def stack_from_table(table):
	table = [line[1::4] for line in table.split('\n')[:-1]]
	stacks = [[] for _ in table[0]]
	for line in table:
		for i, c in enumerate(line):
			if c != ' ':
				stacks[i].append(c)
	return stacks


def do_move1(stacks, move):
	qty, send, dest = move
	stacks[dest-1] = list(reversed(stacks[send-1][:qty])) + stacks[dest-1]
	stacks[send-1] = stacks[send-1][qty:]


def do_move2(stacks, move):
	qty, send, dest = move
	stacks[dest-1] = stacks[send-1][:qty] + stacks[dest-1]
	stacks[send-1] = stacks[send-1][qty:]

#################################################

with open(advent.fname(5)) as f:
	table, moves = f.read().split('\n\n')
moves = moves.split('\n')[:-1]
moves = [[int(nb) for nb in line.split(' ')[1::2]] for line in moves]

stacks1 = stack_from_table(table)
stacks2 = list(stacks1)
for move in moves:
	do_move1(stacks1, move)
	do_move2(stacks2, move)

advent.result(''.join(s[0] for s in stacks1))
advent.result(''.join(s[0] for s in stacks2))
