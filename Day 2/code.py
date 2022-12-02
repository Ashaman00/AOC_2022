import pyperclip

def result(r, n=[1]):
	print(f'Part {n[0]}: {r}')
	n[0] += 1
	pyperclip.copy(r)


def to_integer(p1, p2):
	return ord(p1) - ord('A'), ord(p2) - ord('X')


def outcome(p1, p2):
	if p1 == p2: # draw
		return 3
	if p1 == (p2 + 1) % 3: # lose
		return 0
	return 6 # win


def score1(line):
	p1, p2 = to_integer(*line.split())
	return 1 + p2 + outcome(p1, p2)

#########################################

def choice(p1, cond):
	if cond == 1: # draw
		return p1
	if cond == 2: # win
		return (p1+1) % 3
	return (p1 + 2) % 3 # lose


def score2(line):
	p1, cond = to_integer(*line.split())
	return 1 + choice(p1, cond) + cond * 3

#########################################

with open("input.txt") as f:
	lines = f.readlines()

tot1 = sum(score1(line) for line in lines)
tot2 = sum(score2(line) for line in lines)

result(tot1)
result(tot2)