class Node(object):
	def __init__(self, val):
		self.val = val
		self.children = []
		self.right = None

def connect_siblings(root):
	if not root.children: return
	# connect children firsrt
	for i in xrange(len(root.children)-1):
		curr = root.children[i]
		next = root.children[i+1]
		curr.right = next
	last_child = root.children[-1]
	curr = root.right
	while curr:
		if len(curr.children) > 0:
			last_child.right = curr.children[0]
			break
		curr = curr.right
	# recurse
	for c in root.children:
		connect_siblings(c)

# helper function to return connected siblings as array for testing
def get_connected_siblings(curr):
	res = []
	while curr:
		res.append(curr.val)
		curr = curr.right
	return res

# create tree according to given sample
r = Node(1)
r.children = [Node(2), Node(3), Node(4)]
r.children[0].children = [Node(5), Node(6)]
r.children[2].children = [Node(7)]

# connect siblings!
connect_siblings(r)

# testing
assert get_connected_siblings(r.children[0]) == [2, 3, 4]
assert get_connected_siblings(r.children[0].children[0]) == [5, 6, 7]
