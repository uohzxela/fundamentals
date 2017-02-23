import random

def online_sampling(stream, k):
	sample = []
	num_seen = 0
	for x in stream:
		if len(sample) < k:
			sample.append(x)
		else:
			idx = random.randint(0, num_seen)
			if idx < k:
				sample[idx] = x
		num_seen += 1
	return sample

print online_sampling([x for x in xrange(100)], 10)
