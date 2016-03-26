def run_length_encoding_plus(s):
	block = len(s) - 2
	if block < 2: return
	for b in xrange(block, 1, -1):
		for i in xrange(1,  len(s)-b):
			print s[:i] + str(b) + s[i+b:]

run_length_encoding_plus("nailed")