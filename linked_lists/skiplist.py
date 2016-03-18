import random

class Node(object):
	def __init__(self, val, levels):
		self.val = val
		self.next = [None for i in xrange(levels)]

class SkipList(object):
	def __init__(self):
		self.MAX_LEVEL = 33
		self.head = Node(0, self.MAX_LEVEL)
		self.levels = 1

	def contains(self, val):
		curr = self.head
		for i in xrange(self.levels-1, -1, -1):
			while curr.next[i]:
				if curr.next[i].val > val: break
				if curr.next[i].val == val: return True
				curr = curr.next[i]
		return False

	def insert(self, val):
		levels = 1
		while random.randint(0,9) % 2 == 0 and levels != self.MAX_LEVEL:
			levels += 1
		self.levels = max(self.levels, levels)
		new_node = Node(val, levels)
		curr = self.head
		for i in xrange(self.levels-1, -1, -1):
			while curr.next[i] and curr.next[i].val <= val:
				curr = curr.next[i]
			if i < levels:
				new_node.next[i] = curr.next[i]
				curr.next[i] = new_node

	def delete(self, val):
		curr = self.head
		for i in xrange(self.levels-1, -1, -1):
			while curr.next[i]:
				if curr.next[i].val > val: break
				if curr.next[i].val == val:
					curr.next[i] = curr.next[i].next[i]
					return
				
				curr = curr.next[i]

sl = SkipList()
sl.insert(1)
sl.insert(3)
sl.insert(5)
sl.insert(0)

print sl.contains(1)
print sl.contains(4)
print sl.contains(3)
print sl.contains(5)
print sl.contains(0)

sl.delete(3)
print sl.contains(3)
sl.delete(0)
print sl.contains(0)