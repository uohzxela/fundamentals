from collections import defaultdict

def can_form_palin(s):
	ht = defaultdict(int)
	for c in s:
		ht[c] += 1
	odd_count = 0
	for c in ht:
		if ht[c] % 2 == 1:
			odd_count += 1
		if odd_count > 1:
			return False
	return True

assert can_form_palin("edified")
assert not can_form_palin("hello")
assert can_form_palin("babanan")