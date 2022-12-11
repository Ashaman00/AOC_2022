import advent
from dataclasses import dataclass


@dataclass
class Directory:
	name: str
	parent: 'Directory'
	subdirs: dict[str, 'Directory']
	files: list[tuple[int, str]]

	def root(self):
		if self.parent is None:
			return self
		return self.parent.root()

	def size(self):
		return sum(f[0] for f in self.files) + \
			sum(d.size() for d in self.subdirs.values())

	def all_subs(self):
		yield from self.subdirs.values()
		for d in self.subdirs.values():
			yield from d.all_subs()


def cd(args, out, cwd):
	assert(len(out) == 0 and len(args) == 1)
	if args[0] == '..':
		return cwd.parent
	if args[0] == '/':
		return cwd.root()
	return cwd.subdirs[args[0]]


def ls(args, out, cwd):
	assert(len(args) == 0)
	for line in out:
		p, name = line.strip().split()
		if p == 'dir':
			cwd.subdirs[name] = Directory(name, cwd, subdirs={}, files=[])
		else:
			cwd.files.append((int(p), name))
	return cwd


commands = {
	"ls": ls,
	"cd": cd
}


def recv_command(comm, cwd):
	cc, *output = comm.split('\n')
	name, *args = cc.strip().split(' ')
	return commands[name](args, output, cwd)


def populate_dir(root, comms):
	cwd = root
	for comm in comms:
		cwd = recv_command(comm, cwd)

#################################################


with open(advent.fname(7)) as f:
	comms = f.read()[1:-1].split('\n$')

root = Directory("/", None, subdirs={}, files=[])
populate_dir(root, comms)

res1 = sum(d.size() for d in root.all_subs() if d.size() < 100000)
advent.result(res1)

max_space = 70000000 - 30000000
to_delete = root.size() - max_space
res2 = min(d.size() for d in root.all_subs() if d.size() >= to_delete)
advent.result(res2)
