from collections import deque, defaultdict

D = ['bat', 'cot', 'dog', 'dag', 'dot', 'cat']

def transform_string(D, s1, s2):
	G = make_graph(D)
	q = deque([(s1, 1)])
	visited = defaultdict(lambda: None)
	visited[s1] = True
	while q:
		s, i = q.pop()
		if s == s2:
			return i
		for neighbor in G[s]:
			if visited[neighbor]:
				continue
			visited[neighbor] = True
			q.append((neighbor, i+1))
	return -1

def make_graph(D):
	G = defaultdict(list)
	for i in xrange(len(D)):
		curr = D[i]
		for j in xrange(i+1, len(D)):
			neighbor = D[j]
			if diff_by_one(curr, neighbor):
				G[curr].append(neighbor)
				G[neighbor].append(curr)
	return G

def diff_by_one(s1, s2):
	diff = 0
	for i in xrange(len(s1)):
		if s1[i] != s2[i]:
			diff += 1
		if diff > 1:
			return False
	return diff == 1

assert transform_string(D, 'cat', 'dog') == 4
assert transform_string(D, 'dot', 'dag') == 3
assert transform_string(D, 'dot', 'tag') == -1