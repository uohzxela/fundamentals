class HashSet(object):
	def __init__(self, capacity=1000):
		self.capacity = capacity
		self.buckets = [[] for i in xrange(self.capacity)]
		self.keys = []

	def hash(self, key):
		return sum([ord(c) for c in key]) % self.capacity

	def add(self, key):
		bucket = self.buckets[self.hash(key)]
		for i in xrange(len(bucket)):
			if bucket[i] == key:
				return
		bucket.append(key)
		self.keys.append(key)

	def remove(self, key):
		bucket = self.buckets[self.hash(key)]
		for i in xrange(len(bucket)):
			if bucket[i] == key:
				bucket.remove(bucket[i])
				self.keys.remove(key)
				return
		raise KeyError(key)

	def contains(self, key):
		bucket = self.buckets[self.hash(key)]
		for i in xrange(len(bucket)):
			if bucket[i] == key:
				return True
		return False

	def __contains__(self, key):
		return self.contains(key)

	def __repr__(self):
		string = []
		for k in self.keys:
			string.append(k)
		return '\n'.join(string)

h = HashSet()
h.add("alex")
assert "alex" in h
h.add("xela")
assert "xela" in h
h.remove("alex")
assert "alex" not in h
h.add("vera")
print h