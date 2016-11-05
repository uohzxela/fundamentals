from collections import deque

def bfs(g):
	visited = set()
	q = deque()

	for v in g:
		if v in visited:
			continue
		visited.add(v)
		q.append(v)
		while q:
			v = q.popleft()
			# don't mark it as visited after removing from queue
			# or else there will bugs related to duplicate nodes!
			print v,
			for n in g[v]:
				if n in visited:
					continue
				# important! 
				# mark neighbor as visited before pushing it into queue
				# this is to avoid duplicate neighbors being pushed into the queue
				# in the following iterations of while loop
				visited.add(n)
				q.append(n)

g2 = {
    0 : [1,2,3],
    1 : [4,5],
    2 : [],
    3 : [],
    4 : [],
    5 : []
}

bfs(g2)