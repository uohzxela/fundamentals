def permutations(a):
	permutations_(a, 0)

def permutations_(a, p):
	if p >= len(a):
		print a
		return
	for i in xrange(p, len(a)):
		a[i], a[p] = a[p], a[i]
		permutations_(a, p+1)
		a[i], a[p] = a[p], a[i]

permutations([1,2,3])
