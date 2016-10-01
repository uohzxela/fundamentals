def is_letter_constructible(letter, magazine):
	letter_ht = {}
	# use hash table for the smaller dataset first
	for c in letter:
		if c not in letter_ht:
			letter_ht[c] = 0
		letter_ht[c] += 1
	for c in magazine:
		if c in letter_ht:
			letter_ht[c] -= 1
			if letter_ht[c] == 0:
				del letter_ht[c]
		if len(letter_ht) == 0:
			return True
	return len(letter_ht) == 0