'''
create an array of 2^16 32-bit integers
for every integer in the file, take its 16 most significant bits to index into this array and increment count
since the file contains less than 2^32 numbers, there must be one entry in the array that is less than 2^16
this tells us that there is at least one integer which has those upper bits and is not in the file
in the second pass, we focus only on the integers whose leading 16 bits match the one we have found
and use a bit array of size 2^16 to identify a missing address

'''

def search(file):
	count = [0 for i in xrange(2^16)]
	for e in file:
		count[e >> 16] += 1 
	for i in xrange(len(count)):
		c = count[i]
		bitset = [False for i in xrange(2^16)]
		if c < 2^16: 
			for e in file:
				if e >> 16 == i:
					'''
					2^16-1 is used to mask off the upper 16 bits so that 
					only the lower 16 bits can be obtained

					why minus 1? e.g. 2^4 = 10000, 2^4-1 = 01111
					
					'''
					bitset[2^16-1 & e] = True
			for j in xrange(2^16):
				if not bitset[j]: return i << 16 | j