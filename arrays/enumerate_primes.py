def enum_primes(n):
	primes = []
	is_primes = [True for i in xrange(n+1)]
	for i in xrange(2, n+1):
		if is_primes[i]:
			for j in xrange(i*i, n+1, i):
				is_primes[j] = False
			primes.append(i)
	return primes

assert enum_primes(200) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 
 163, 167, 173, 179, 181, 191, 193, 197, 199]
assert enum_primes(18) == [2, 3, 5, 7, 11, 13, 17]
