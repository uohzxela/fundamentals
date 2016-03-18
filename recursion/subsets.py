# version 1
def subsets(A):
	print_subsets(A, A, 0, 0)

def print_subsets(set, subset, r, w):
	if r == len(set):
		print_subset(subset, w)
		return
	print_subsets(set, subset, r+1, w)
	subset[w], set[r] = set[r], subset[w]
	print_subsets(set, subset, r+1, w+1)
	subset[w], set[r] = set[r], subset[w]

def print_subset(subset, w):
	print subset[:w]

subsets([1,2,3])

print

def subsets2(A):
	print_subsets2(A, [False]*len(A), 0)

def print_subsets2(set, subset, k):
	if k == len(set):
		print_subset2(set, subset)
		return
	print_subsets2(set, subset, k+1)
	subset[k] = True
	print_subsets2(set, subset, k+1)
	subset[k] = False

def print_subset2(set, subset):
	print '{',
	for i in xrange(len(subset)):
		if subset[i]: print set[i],
	print '}'

subsets2([1,2,3])