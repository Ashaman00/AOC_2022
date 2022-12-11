import advent

with open(advent.fname(1)) as f:
	maxi, cur = [0, 0, 0], 0
	for line in f.read().split('\n'):
		if line == '':
			maxi.append(cur)
			maxi = sorted(maxi, key=lambda x: -x)[:-1]
			cur = 0
		else:
			cur += int(line)

advent.result(maxi[0])
advent.result(sum(maxi))
