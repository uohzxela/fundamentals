def array_product(a):
	p = 1
	product = [1 for i in xrange(len(a))]
	for i in xrange(len(a)):
		product[i] = p
		p *= a[i]
	p = 1
	for i in xrange(len(a)-1, -1, -1):
		product[i] *= p
		p *= a[i]
	return product

print array_product([1,2,3,4,5])