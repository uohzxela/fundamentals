def hamming(n):
	count = 0
	while n:
		count += (n & 1 )
		n = n >> 1
	return count

def hammingArr(A):
	return sum(map(hamming, A))
	
print hammingArr([31,51])