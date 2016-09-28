B = 1
W = 0
G = 2

M = [
[B, B, B, B],
[W, B, W, B],
[B, W, W, B],
[B, B, B, B]
]

M2 = [
[B, B, B, B, B],
[W, W, B, W, B],
[W, W, B, W, B],
[B, B, W, W, B],
[B, W, B, B, W]
]

def fill_enclosed_regions(M):
	mark_non_enclosed_regions(M)
	fill_enclosed_regions_(M)

def mark_non_enclosed_regions(M):
	for i in xrange(len(M[0])):
		if M[0][i] == W:
			dfs(M, 0, i)
		if M[len(M)-1][i] == W:
			dfs(M, len(M)-1, i)
	for i in xrange(len(M)):
		if M[i][0] == W:
			dfs(M, i, 0)
		if M[i][len(M[0])-1] == W:
			dfs(M, i, len(M)[0]-1)

def dfs(M, x, y):
	M[x][y] = G
	for x, y in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
		if x < 0 or x > len(M)-1 or y < 0 or y > len(M[0])-1:
			continue
		if M[x][y] != W:
			continue
		dfs(M, x, y)

def fill_enclosed_regions_(M):
	for i in xrange(len(M)):
		for j in xrange(len(M[0])):
			if M[i][j] == W:
				M[i][j] = B
			elif M[i][j] == G:
				M[i][j] = W

def print_matrix(M):
	for i in xrange(len(M)):
		for j in xrange(len(M[0])):
			print M[i][j],
		print
	print

print_matrix(M)
fill_enclosed_regions(M)
print_matrix(M)

print_matrix(M2)
fill_enclosed_regions(M2)
print_matrix(M2)