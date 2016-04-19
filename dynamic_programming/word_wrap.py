
def minimumMessiness(words, lineLength):
	minMessiness = [float('inf') for i in xrange(len(words))]
	numRemainingBlanks = lineLength - len(words[0])
	minMessiness[0] = numRemainingBlanks * numRemainingBlanks
	for i in xrange(1, len(words)):
		numRemainingBlanks = lineLength - len(words[i])
		minMessiness[i] = minMessiness[i-1] + numRemainingBlanks * numRemainingBlanks
		# try adding words[i-1], words[i-2]...
		for j in xrange(i-1, -1, -1):
			numRemainingBlanks -= len(words[j]) + 1
			if numRemainingBlanks < 0:
				break
			firstJMessiness = minMessiness[j-1] if j-1 >= 0 else 0
			currLineMessiness = numRemainingBlanks * numRemainingBlanks
			minMessiness[i] = min(minMessiness[i], firstJMessiness + currLineMessiness)
	return minMessiness[-1]


s = "Geeks for Geeks presents word wrap problem"
print minimumMessiness(s.split(" "), 15)
