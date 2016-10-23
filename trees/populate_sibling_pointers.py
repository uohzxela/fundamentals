class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.next = None

r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)
r.right.left = Node(6)
r.right.right = Node(7)

def populate(root):
	if not root:
		return
	if root.left:
		root.left.next = root.right
	if root.right and root.next:
		root.right.next = root.next.left
	populate(root.left)
	populate(root.right)

def printNext(curr):
	while curr is not None:
		print curr.val, "->",
		curr = curr.next
	print "None"

populate(r)

printNext(r)
printNext(r.left)
printNext(r.left.left)
