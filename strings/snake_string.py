s = "Google Worked"
def printSnakeString(s):
	printTop(s)
	printMiddle(s)
	printBottom(s)
	
def printTop(s):
	print "   ",
	for i in xrange(2, len(s), 4):
		c = s[i] if s[i] != ' ' else '~'
		print c + "      ",
	print

def printMiddle(s):
	print " ",
	for i in xrange(1, len(s), 2):
		c = s[i] if s[i] != ' ' else '~'
		print c + "  ",
	print

def printBottom(s):
	for i in xrange(0, len(s), 4):
		c = s[i] if s[i] != ' ' else '~'
		print c + "      ",
	print

printSnakeString(s)