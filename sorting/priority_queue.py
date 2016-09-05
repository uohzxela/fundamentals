PQ_SIZE = 1000

# also known as min heap
class PriorityQueue:
	def __init__(self):
		self.capacity = PQ_SIZE
		self.n = 0
		self.q = []

	"""Time complexity: O(n)"""
	def heapify(self, arr):
	# arr is an array with arbitrarily placed elements
	# the observation is that any element that is indexed after self.n/2-1 is a leaf node
	# hence it is a one-element heap,
	# so we only need to bubble down the non-leaf nodes before the index
		self.q = arr
		self.n = len(arr)
		for i in xrange(self.n/2-1, -1, -1):
			self.bubble_down(i)

	"""Time complexity: O(nlog n)"""
	def insert(self, x):
		if self.n >= PQ_SIZE:
			print  "Warning: priority queue overflow insert"
		else:
			self.q.append(x)
			self.bubble_up(self.n)
			self.n += 1

	"""Time complexity: O(1)"""
	def swap(self, i, j):
		self.q[i], self.q[j] = self.q[j], self.q[i]

	"""Time complexity: O(log n)"""
	def bubble_up(self, i):
		parent = (i-1)/2
		if parent < 0: return
		if self.q[parent] > self.q[i]:
			self.swap(parent, i)
			self.bubble_up(parent)

	"""Time complexity: O(log n)"""
	def bubble_down(self, i):
		left = 2*i+1
		right = 2*i+2
		min_idx = i
		
		if left < self.n and self.q[left] < self.q[min_idx]:
			min_idx = left
		if right < self.n and self.q[right] < self.q[min_idx]:
			min_idx = right
		if min_idx != i:
			self.swap(min_idx, i)
			self.bubble_down(min_idx)

	"""Time complexity: O(log n)"""
	def extract_min(self):
		if self.n <= 0: 
			print "Warning: empty priority queue"
		else:
			min = self.q[0]
			self.q[0] = self.q[self.n-1]
			self.n -= 1
			self.bubble_down(0)
		return min 

