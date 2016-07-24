def can_reach_end(A):
	furthest_step = 0
	for i in xrange(len(A)):
		if i > furthest_step: return False
		furthest_step = max(furthest_step, i + A[i])
	return furthest_step >= len(A) - 1

assert can_reach_end([3,3,1,0,2,0,1]) == True
assert can_reach_end([3,2,0,0,2,0,1]) == False