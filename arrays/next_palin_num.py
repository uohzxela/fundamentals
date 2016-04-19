# first loop is to mirror the right side with left by adding numbers
# second loop is necessary as some carry digits overflowed into the left side during the first loop
# therefore the right side needs to be mirrored with left again
# no third loop necessary since all carry digits have been propagated after the first loop

def nextPalinNum(num):
	return nextPalinNum_(nextPalinNum_(num+1))

def nextPalinNum_(num):
	n = len(str(num))
	for i in xrange(n/2):
		numStr = str(num)
		left = int(numStr[i]) + 10
		right = int(numStr[n-i-1])	
		numToAdd = (left - right)%10
		num += numToAdd * pow(10, i)
	return num

print nextPalinNum(999)
print nextPalinNum(23545)
print nextPalinNum(1234)
print nextPalinNum(1997)
print nextPalinNum(4512)
print nextPalinNum(6789876)
print nextPalinNum(4512)
print nextPalinNum(6791976)
print nextPalinNum(2788)
print nextPalinNum(94187978322)
print nextPalinNum(1234628)
print nextPalinNum(713322)
print nextPalinNum(1111)
