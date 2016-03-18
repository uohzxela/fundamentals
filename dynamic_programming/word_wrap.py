# my valiant attempt, but failed during memoization part
def word_wrap(words, s, i, cost, limit, c):
	POW = 2
	if (s, i) not in c:
		if i == len(words):
			# print remaining_spaces
			remaining_spaces = limit - (i - s) 
			# print remaining_spaces
			if remaining_spaces >= 0: 
				c[(s,i)] = cost + pow(remaining_spaces, POW)
				return cost + pow(remaining_spaces, POW)
			else: 
				c[(s,i)] = float('inf')
				return float('inf')

		if (words[i] == ' '):
			# print remaining_spaces
			remaining_spaces = (limit - (i - s))
			if remaining_spaces  >= 0:
				cost1 = word_wrap(words, i+1, i+1, cost + pow(remaining_spaces, POW), limit,c)
				cost2 = word_wrap(words, s, i+1, cost, limit,c)
				# print cost2
				c[(s,i)] = min(cost1, cost2)
				return min(cost1, cost2)
			else:
				c[(s,i)] = float('inf')
				return float('inf')
		else:
			c[(s,i)] = word_wrap(words, s, i+1, cost, limit,c)
			return c[(s,i)]
	else:
		return c[(s,i)]

def wwrap(words, k):
	cache = {}
	print word_wrap(words, 0, 0, 0, k, cache)

###############################################################################

def solve(L, limit):
    L = map(lambda x: len(x), L.split(" "))
    # print L
    n = len(L)
    # extras[i][j] will have number of extra spaces if words from i to j are put in a single line
    extras = [[0 for j in xrange(n+1)] for i in xrange(n+1)]
    # lc[i][j] will have cost of a line which has words from i to j
    lc = [[0 for j in xrange(n+1)] for i in xrange(n+1)]
    # c[i] will have total cost of optimal arrangement of words from 1 to i
    c = [0 for i in xrange(n+1)]

    for i in xrange(1,n+1):
    	extras[i][i] = limit - L[i-1]
    	for j in xrange(i+1, n+1):
    		extras[i][j] = extras[i][j-1] - L[j-1] - 1

    for i in xrange(1, n+1):
    	for j in xrange(i, n+1):
    		if extras[i][j] < 0:
    			lc[i][j] = float('inf')
    		elif j == n and extras[i][j] >= 0:
    			lc[i][j] = pow(extras[i][j], 2)
    			# debatable whether to use 0 for last line
    			# lc[i][j] = 0
    		else:
    			lc[i][j] = pow(extras[i][j], 2)
    c[0] = 0
    for j in xrange(1,n+1):
    	c[j] = float('inf')
    	for i in xrange(1, j+1):
    		if (c[i-1] != float('inf') and lc[i][j] != float('inf') and
    			(c[i-1] + lc[i][j]) < c[j]):
    			c[j] = c[i-1] + lc[i][j]

    print c[-1]

s = "Geeks for Geeks presents word wrap problem"
# s = "aaa bb cc ddddd"
wwrap(s, 15)
solve(s, 15)
