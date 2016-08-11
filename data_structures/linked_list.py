class LinkedList(object):
	def __init__(self):
		self.head = None
		self.size = 0

	def insert_beginning(self, val):
		"""Time complexity: O(1)"""
		node = Node(val)
		node.next = self.head
		self.head = node
		self.size += 1

	def remove(self, val):
		"""Time complexity: O(n)"""
		prev = None
		curr = self.head
		while curr:
			if curr.val == val:
				if prev is None:
					self.head = curr.next
				else:
					prev.next = curr.next
				self.size -= 1
				return True
			prev = curr
			curr = curr.next
		return False

	def contains(self, val):
		"""Time complexity: O(n)"""
		curr = self.head
		while curr:
			if curr.val == val:
				return True
			curr = curr.next
		return False

	def print_list(self):
		curr = self.head
		while curr:
			print curr.val,
			curr = curr.next
		print

	def get_size(self):
		return self.size


class Node(object):
	def __init__(self, val=None, next=None):
		self.val = val
		self.next = next

llist = LinkedList()
llist.insert_beginning(1)
llist.insert_beginning(2)
llist.insert_beginning(3)
llist.insert_beginning(4)
llist.print_list()
assert llist.contains(2)
print "After removing 2"
llist.remove(2)
llist.print_list()
assert not llist.contains(2)
assert llist.get_size() == 3