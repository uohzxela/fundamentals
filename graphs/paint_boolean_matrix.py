from collections import deque, defaultdict

M = [
[0, 1, 1, 1, 1],
[1, 0, 0, 0, 0],
[1, 0, 0, 1, 0],
[0, 0, 1, 0, 1],
[1, 0, 1, 0, 1]
]

M2 = [
[0, 1],
[0, 0]
]
def paint(M, x, y):
	q = deque([(x, y)])
	prev_color = M[x][y]
	M[x][y] ^= 1
	while q:
		x, y = q.popleft()
		for i, j in [(x, y-1), (x, y+1), (x+1, y), (x-1, y)]:
			if i < 0 or i > len(M)-1 or j < 0 or j > len(M[0])-1:
				continue
			if M[i][j] != prev_color:
				continue
			# must flip current cell before pushing to queue
			# so as to mark it as visited
			q.append((i, j))
			M[i][j] ^= 1

def print_matrix(M):
	for i in xrange(len(M)):
		for j in xrange(len(M[0])):
			print M[i][j],
		print
	print

print_matrix(M)
paint(M, 2, 2)
print_matrix(M)