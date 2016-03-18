def quicksort(A):
	quicksort_(A, 0, len(A)-1)

def quicksort_(A, s, e):
	if s < e:
		p = partition(A, s, e)
		quicksort_(A, s, p-1)
		quicksort_(A, p+1, e)

def partition(a, s, e):
	p = e
	firsthigh = s
	for i in xrange(s, e):
		if a[i] < a[p]:
			a[firsthigh], a[i] = a[i], a[firsthigh]
			firsthigh += 1
	a[p], a[firsthigh] = a[firsthigh], a[p]
	return firsthigh

A = [23, 21, 5, 9, 10, 4, 1, 1, 1, 1, 1, 1, 8, 3, 0,-1, -10]
quicksort(A)
print A