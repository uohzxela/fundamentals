from utils import printTree, findLen

class Tree(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

r1 = Tree(2)
r1.left = Tree(1)
r1.right = Tree(3)

r2 = Tree(7)
r2.left = Tree(6)
r2.right = Tree(8)


def flatten(root):
	if not root: return None
	h, t = flatten_(root)
	return h

def flatten_(root):
	left_h = right_t = root
	if root.left:
		left_h, left_t = flatten_(root.left)
		left_t.next = root
	if root.right:
		right_h, right_t = flatten_(root.right)
		root.next = right_h
		right_t.next = None
	root.left = root.right = None
	return left_h, right_t

def merge(h1, h2):
	fake_head = Tree(None)
	p1, p2, p = h1, h2, fake_head
	while p1 and p2:
		if p1.val <= p2.val:
			p.next = p1
			p1 = p1.next
		else:
			p.next = p2
			p2 = p2.next
		p = p.next

	if p1: p.next = p1
	if p2: p.next = p2

	return fake_head.next

def find_middle(h):
	slow = fast = h
	prev = None
	while fast and fast.next:
		prev = slow 
		slow = slow.next
		fast = fast.next.next
	return prev, slow


def balance_(h, n):
	if n <= 0: return None, h
	left_child, curr_root = balance_(h, n/2)
	curr_root.left = left_child
	right_child, next_root = balance_(curr_root.next, n-n/2-1)
	curr_root.right = right_child
	return curr_root, next_root


def balance(h):
	n = findLen(h)
	return balance_(h, n)[0]

h1 = flatten(r1)
h2 = flatten(r2)
h = merge(h1, h2)
r = balance(h)
printTree(r)