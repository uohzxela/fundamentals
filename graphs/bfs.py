from collections import defaultdict, deque
def bfs(g):
	visited = defaultdict(lambda: None)
	q = deque()

	for v in g:
		if not visited[v]:
			q.append(v)
		while q:
			n = q.popleft()
			# don't mark it as visited after removing from queue
			# or else there will bugs related to duplicate nodes!
			print n,
			for neighbor in g[n]:
				if visited[neighbor]:
					continue
				# important! 
				# mark neighbor as visited before pushing it into queue
				# this is to avoid duplicate neighbors being pushed into the queue
				# in the following iterations of while loop
				visited[n] = True
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