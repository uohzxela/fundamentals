def enumeratePrimes(n):
	primes = [True for i in xrange(n+1)]
	primes[0] = primes[1] = False
	for i in xrange(2, n+1):
		if primes[i]:
			print 'i:', i
			j = i*i
			while j < n+1:
				print 'j:', j
				primes[j] = False
				j += i
	for i in xrange(n+1):
		if primes[i]:
			print i,
	print


enumeratePrimes(168)