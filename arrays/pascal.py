def pascal(n):
	arr = []
	for line in xrange(1,n+1):
		c = 1
		for i in xrange(1, line+1):
			print c,
			c = c * (line - i)/i
		print 

pascal(6)
