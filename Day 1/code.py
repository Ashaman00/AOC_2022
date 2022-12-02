import pyperclip

def result(r, n=[1]):
	print(f'Part {n[0]}: {r}')
	n[0] += 1
	pyperclip.copy(r)


with open("input.txt") as f:
	maxi, cur = [0,0,0], 0
	for line in f.read().split('\n'):
		if line == '':
			maxi.append(cur)
			maxi = sorted(maxi, key=lambda x: -x)[:-1]
			cur = 0
		else:
			cur += int(line)

result(maxi[0])
result(sum(maxi))