PQ_SIZE = 1000

# also known as min heap
class PriorityQueue:
	def __init__(self):
		self.capacity = PQ_SIZE
		self.n = 0
		self.q = []

	def insert(self, x):
		if self.n >= PQ_SIZE:
			print  "Warning: priority queue overflow insert"
		else:
			self.q.append(x)
			self.bubble_up(self.n)
			self.n += 1

	def swap(self, i, j):
		self.q[i], self.q[j] = self.q[j], self.q[i]

	def bubble_up(self, i):
		parent = (i-1)/2
		if parent == -1: return
		if self.q[parent] > self.q[i]:
			self.swap(parent, i)
			self.bubble_up(parent)

	def bubble_down(self, i):
		left = 2*i+1
		right = 2*i+2
		min = i
		
		if left < self.n and self.q[left] < self.q[min]:
			min = left
		if right < self.n and self.q[right] < self.q[min]:
			min = right
		if min != i:
			self.swap(min, i)
			self.bubble_down(min)

	def extract_min(self):
		if self.n <= 0: 
			print "Warning: empty priority queue"
		else:
			min = self.q[0]
			self.q[0] = self.q[self.n-1]
			self.n -= 1
			self.bubble_down(0)
		return min 

