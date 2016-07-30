def enumeratePrimes(n):
	primes = [True for i in xrange(n+1)]
	for i in xrange(2, n+1):
		if primes[i]:
			for j in xrange(i*i, n+1, i):
				primes[j] = False
			print i,
	print

enumeratePrimes(200)