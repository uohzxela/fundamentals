from collections import defaultdict

G = defaultdict(list)

G[5] = [11]
G[7] = [11, 8]
G[3] = [8, 10]
G[11] = [2, 9, 10]
G[8] = [9]
G[2] = []
G[9] = []
G[10] = []

def toposort(G):
	visited = set()
	stack = []
	for v in G:
		if v in visited:
			continue
		toposort_(G, v, visited, stack)
	while stack:
		print stack.pop(),
	print

def toposort_(G, v, visited, stack):
	visited.add(v)
	for n in G[v]:
		if n in visited:
			continue
		toposort_(G, n, visited, stack)
	stack.append(v)

toposort(G)
