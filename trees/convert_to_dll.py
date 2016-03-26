class Tree(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.right = None

r = Tree(4)
r.left = Tree(2)
r.left.left = Tree(1)
r.left.right = Tree(3)
r.right = Tree(6)
r.right.left = Tree(5)


def flatten(root):
	h, t = flatten_(root)
	h.prev = t 
	t.next = h
	return h

def flatten_(root):
	left_h = right_t = root
	if root.left:
		left_h, left_t = flatten_(root.left)
		left_t.next = root
		root.prev = left_t
	if root.right:
		right_h, right_t = flatten_(root.right)
		right_h.prev = root
		root.next = right_h
		right_t.next = None
	return left_h, right_t

def print_forward_loop(h):
	curr = h
	for _ in xrange(15):
		print curr.val,
		curr = curr.next
	print

def print_reverse_loop(h):
	curr = h
	for _ in xrange(15):
		print curr.val,
		curr = curr.prev
	print

h = flatten(r)
print_forward_loop(h)
print_reverse_loop(h)