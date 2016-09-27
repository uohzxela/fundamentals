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
	path = [(len(M)-1, 0)]
	if search_maze_(M, len(M)-1, 0, path):
		print path
	else:
		print "No path found."

def search_maze_(M, x, y, path):
	# found exit
	if x == 0 and y == len(M[0])-1:
		return True
	for i, j in [(x, y-1), (x, y+1), (x+1, y), (x-1, y)]:
		# check if (x,y) exceeds boundary
		if i < 0 or i > len(M)-1 or j < 0 or j > len(M[0])-1:
			continue
		if M[i][j] == BLOCKED:
			continue
		path.append((i, j))
		# set current cell to BLOCKED to avoid visiting it again
		# or you can pass in a "visited" hashmap as an extra param
		M[i][j] = BLOCKED
		if search_maze_(M, i, j, path):
			return True
		# remember to backtrack!
		path.pop()
	return False

search_maze(M)