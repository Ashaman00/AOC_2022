import advent

def distinct_chars_pos(line, nb_chars):
	for pos in range(nb_chars-1, len(line)):
		if len(set(line[pos-nb_chars:pos])) == nb_chars:
			return pos

#################################################

with open(advent.fname(6)) as f:
	line = f.read()

advent.result(distinct_chars_pos(line, 4))
advent.result(distinct_chars_pos(line, 14))
