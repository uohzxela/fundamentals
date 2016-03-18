def mergesort(a):
	if len(a) <= 1: return a 
	m = len(a)/2 
	left = mergesort(a[:m])
	right = mergesort(a[m:])
	return merge(left, right)


def merge(a1, a2):
	p1 = p2 = 0
	res = []
	while p1 < len(a1) and p2 < len(a2):
		if a1[p1] <= a2[p2]:
			res.append(a1[p1])
			p1 += 1
		else:
			res.append(a2[p2])
			p2 += 1
	res += a1[p1:]
	res += a2[p2:]
	return res 

print mergesort([23, 21, 5, 9, 10, 4, 1, 8, 3, 0,-1, -10])