def mergesort(A):
	if len(A) <= 1:
		return A
	m = len(A)/2
	left = mergesort(A[:m])
	right = mergesort(A[m:])
	return merge(left, right)

def merge(left, right):
	res = []
	n, m = 0, 0
	while n < len(left) and m < len(right):
		if left[n] <= right[m]:
			res.append(left[n])
			n += 1
		else:
			res.append(right[m])
			m += 1
	res += left[n:]
	res += right[m:]
	return res 

print mergesort([23, 21, 5, 9, 10, 4, 1, 8, 3, 0,-1, -10])
