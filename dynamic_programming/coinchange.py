def coin_change(n, d):
	min = None 
	for value in d:
		if n-value == 0: return 1
		if n-value > 0:
			ans1 = coin_change(n-value, d)
			if ans1 is not None:
				if min is None or ans1 < min: min = ans1
	return min + 1

d = [1, 5, 10, 25]

print coin_change(29, d)