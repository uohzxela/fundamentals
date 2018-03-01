from collections import defaultdict

M = [
[0, 0, 0, 1, 0],
[0, 1, 0, 0, 0],
[0, 1, 0, 1, 1],
[0, 0, 0, 0, 1],
[0, 1, 0, 1, 0]
]

BLOCKED = 1

def search_maze(M):
	path = [(len(M) - 1, 0)]
	if search(M, len(M) - 1, 0, path):
		print path
	else:
		print 'No path found.'

def search(M, x, y, path):
	if exceeds_boundary(M, x, y) or M[x][y] == BLOCKED:
		return False
	# found exit
	if x == 0 and y == len(M[0]) - 1:
		return True

	# set current cell to BLOCKED to avoid visiting it again
	# or you can pass in 'visited' hashmap as param
	M[x][y] = BLOCKED
 	for i, j in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
		path.append((i, j))
		if search(M, i, j, path):
			return True
		# remember to backtrack!
		path.pop()
	return False

def exceeds_boundary(M, x, y):
	return x < 0 or y < 0 or x > len(M) - 1 or y > len(M[0]) - 1

search_maze(M)
