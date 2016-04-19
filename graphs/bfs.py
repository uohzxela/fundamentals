from collections import defaultdict, deque
def bfs(g):
	visited = defaultdict(lambda: None)
	q = deque()

	for v in g:
		if not visited[v]:
			q.append(v)
		while q:
			n = q.popleft()
			visited[n] = True
			print n,
			for neighbor in g[n]:
				if not visited[neighbor]:
					q.append(neighbor)

g2 = {
    0 : [1,2,3],
    1 : [4,5],
    2 : [],
    3 : [],
    4 : [],
    5 : []
}

bfs(g2)