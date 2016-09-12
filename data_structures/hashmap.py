class HashMap(object):
	def __init__(self, capacity=1000):
		self.capacity = capacity
		self.buckets = [[] for i in xrange(self.capacity)]

	def hash(self, key):
		return sum([ord(c) for c in key]) % self.capacity

	def set(self, key, val):
		bucket = self.buckets[self.hash(key)]
		for i in xrange(len(bucket)):
			k, v = bucket[i]
			if k == key:
				bucket[i] = (key, val)
				return
		bucket.append((key, val))

	def get(self, key):
		bucket = self.buckets[self.hash(key)]
		for i in xrange(len(bucket)):
			k, v = bucket[i]
			if k == key:
				return v
		raise KeyError(key)

	def delete(self, key):
		bucket = self.buckets[self.hash(key)]
		for i in xrange(len(bucket)):
			k, v = bucket[i]
			if k == key:
				bucket.remove(bucket[i])
				return
		raise KeyError(key)

	def contains(self, key):
		bucket = self.buckets[self.hash(key)]
		for i in xrange(len(bucket)):
			k, v = bucket[i]
			if k == key:
				return True
		return False

	def __setitem__(self, key, val):
		self.set(key, val)

	def __getitem__(self, key):
		return self.get(key)

	def __delitem__(self, key):
		self.delete(key)

	def __contains__(self, key):
		return self.contains(key)

	def __repr__(self):
		string = []
		for bucket in self.buckets:
			if not bucket: continue
			string.append(bucket[0][0] + ": " + str(bucket))
		return '\n'.join(string)

h = HashMap()
h["alex"] = "rocks"
h["xela"] = "skcor"
assert h['alex'] == 'rocks'
h['alex'] = 'hello'
assert h['alex'] == 'hello'
assert 'alex' in h
del h['alex']
assert 'alex' not in h
h['vera'] = 'helloz'
print h
