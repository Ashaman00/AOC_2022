import pyperclip
from time import process_time

FULL = '⬜'  # '█'
EMPTY = '  '  # '░'


def result(r, n=[1]):
	t = process_time()
	if t < 10:
		print(f'Part {n[0]}: {r} - ({1000*t:.2f} ms)')
	else:
		print(f'Part {n[0]}: {r} - ({t:.2f} s)')
	n[0] += 1
	pyperclip.copy(r)


def fname(day, test=False):
	if test:
		return f'../inputs/test{day}.txt'
	return f'../inputs/day{day}.txt'
