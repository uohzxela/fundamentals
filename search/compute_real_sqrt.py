SMALLER = -1
LARGER = 1
EQUAL = 0

def sqrt(x):
	x = float(x)
	left = right = None
	# we need to tighten the bounds for more efficient computation
	if (x < 1.):
		# lower and upper bounds of solution space is different for real square roots
		# because sqrt(1/4) = 1/2 which is bigger than 1/4
		left = x
		right = 1.
	else:
		left = 1.
		right = x
	# left - right will always be negative if left < right within a certain threshold
	while compare(left, right) == SMALLER:
		# avoid overflow, which is esp. impt with floating numbers
		mid = left + 0.5 * (right - left)
		mid_sq = mid*mid
		if compare(mid_sq, x) == EQUAL:
			return mid
		elif compare(mid_sq, x) == LARGER:
			right = mid
		else:
			# we are computing real square roots so we need the answer
			# to be as precise as possible, hence we return the most recent mid as what it is
			# compare this with compute_int_sqrt.py
			left = mid
	return left

def compare(a, b):
	EPSILON = 0.00001
	diff = (a - b)
	if diff < -EPSILON:
		return SMALLER
	elif diff > EPSILON:
		return LARGER
	else:
		return EQUAL

print sqrt(7)
print sqrt(4)