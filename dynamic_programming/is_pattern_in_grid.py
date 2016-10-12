def is_pattern_in_grid(grid, pattern):
	res = -1
	dp = [[-1 for j in xrange(len(grid))] for i in xrange(len(grid))]
	for i, p in enumerate(pattern):
		for x in xrange(len(dp)):
			for y in xrange(len(dp)):
				if p == grid[x][y] and has_prefix(dp, x, y, i):
					dp[x][y] = i
					res = max(res, i)
	return res == len(pattern)-1

def has_prefix(dp, x, y, i):
	if x - 1 >= 0 and dp[x-1][y] == i-1:
		return True
	if y - 1 >= 0 and dp[x][y-1] == i-1:
		return True
	if x + 1 < len(dp) and dp[x+1][y] == i-1:
		return True
	if y + 1 < len(dp[0]) and dp[x][y+1] == i-1:
		return True
	return False

grid = [
[1,2,3],
[3,4,5],
[5,6,7]
]

pattern1 = [1,3,4,6]
pattern2 = [1,2,3,4]
pattern3 = [1,2,3,5,7,6,4,2,1]
pattern4 = [1,3,5,6,4,2,3,5,7]
pattern5 = [1,3,5,6,4,2,3,5,7,1]
pattern6 = [1,4]

assert is_pattern_in_grid(grid, pattern1)
assert is_pattern_in_grid(grid, pattern3)
assert is_pattern_in_grid(grid, pattern4)
assert not is_pattern_in_grid(grid, pattern2)
assert not is_pattern_in_grid(grid, pattern5)
assert not is_pattern_in_grid(grid, pattern6)
