from collections import defaultdict

# 1->2->3
g = {
	5: [2, 0],
	4: [0, 1],
	3: [1],
	2: [3]
}

def toposort(g):
	visited = defaultdict(lambda: None)
	stack = []
	for k,v in g.iteritems():
		if not visited[k]:
			toposort_(g, stack, visited, k)
	while stack:
		print stack.pop(),
	print

def toposort_(g, stack, visited, v):
	visited[v] = True
	if v in g:
		for n in g[v]:
			if not visited[n]: 
				toposort_(g, stack, visited, n)
	stack.append(v)

toposort(g)

