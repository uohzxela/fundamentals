def uniform_random(lower_bound, upper_bound):
	num_possibilities = upper_bound - lower_bound + 1
	res = 0
	while True:
		i = 0
		while (1 << i) < num_possibilities:
			res = (res << 1) | zeroOneRandom()
			i += 1
		if res < num_possibilities:
			break
	return res + lower_bound