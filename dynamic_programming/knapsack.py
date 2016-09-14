"""
Write a program for the knapsack problem that selects a subset of items
that has maximum value and satisfies the weight constraint. All item have
integer weights and values. Return the value of the subset.
"""

class Item(object):
	def __init__(self, weight, val):
		self.weight = weight
		self.val = val

def find_optimum_val(capacity, items):
	return find_optimum_val_(capacity, items, len(items)-1, 0)

def find_optimum_val_(capacity, items, i, val):
	if i < 0:
		return val
	item = items[i]
	val1 = find_optimum_val_(capacity, items, i-1, val)
	if item.weight > capacity:
		return val1
	val2 = find_optimum_val_(capacity-item.weight, items, i-1, val+item.val)
	return max(val1, val2)

def find_optimum_valDP(capacity, items):
	dp = [[0 for j in xrange(len(items)+1)] for i in xrange(capacity+1)]
	for i in xrange(1, capacity+1):
		for j in xrange(1, len(items)+1):
			item = items[j-1]
			val1 = dp[i][j-1]
			if item.weight > i:
				dp[i][j] = val1
				continue
			val2 = dp[i-item.weight][j-1] + item.val
			dp[i][j] = max(val1, val2)
	return dp[-1][-1]

items = [Item(5, 60), Item(3, 50), Item(4, 70), Item(2, 30)]
assert find_optimum_val(5, items) == 80
assert find_optimum_valDP(5, items) == 80

