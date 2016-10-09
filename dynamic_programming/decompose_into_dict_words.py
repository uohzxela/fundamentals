from collections import defaultdict

def decompose_into_words(name, dict_words):
	cache = defaultdict(lambda: None)
	return decompose(name, dict_words, len(name)-1, len(name), [], cache)

def decompose(name, dict_words, s, e, words, cache):
	if s <= 0:
		if name[s:e] in dict_words:
			cache[(s,e)] = words + [name[s:e]]
			return words + [name[s:e]]
		return None
	substr = name[s:e]
	res1 = None
	if substr in dict_words:
		if (s-1, s) in cache:
			res1 = cache[(s-1, s)]
		else:
			res1 = decompose(name, dict_words, s-1, s, words+[substr], cache)
			cache[(s-1, s)] = res1
	if (s-1, e) in cache:
		res2 = cache[(s-1, e)]
	else:
		res2 = decompose(name, dict_words, s-1, e, words, cache)
	cache[(s, e)] = res1 or res2
	return res1 or res2

print decompose_into_words("amanaplanacanal", set(['a', 'man', 'plan', 'canal']))
print decompose_into_words("bedbathandbeyond", set(['bed', 'bat', 'hand', 'beyond', 'bath']))

def decompose_into_dict_words(domain, dictionary):
	last_length = [-1 for i in xrange(len(domain))]
	for i in xrange(len(domain)):
		if domain[:i+1] in dictionary:
			last_length[i] = i + 1
		if last_length[i] == -1:
			for j in xrange(i):
				if (last_length[j] != -1 and 
					domain[j+1:i+1] in dictionary):
					last_length[i] = i - j
					break

	decompositions = []
	if last_length[-1] != -1:
		idx = len(domain) - 1
		while idx >= 0:
			decompositions.append(domain[idx - last_length[idx] + 1: idx + 1])
			idx -= last_length[idx]
		decompositions.reverse()
	return decompositions

assert decompose_into_dict_words("amanaplanacanal", set(['a', 'man', 'plan', 'canal'])) == ['a', 'man', 'a', 'plan', 'a', 'canal']
assert decompose_into_words("bedbathandbeyond", set(['bed', 'bat', 'hand', 'beyond', 'bath'])) == ['beyond', 'hand', 'bat', 'bed']