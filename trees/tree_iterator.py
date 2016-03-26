class TreeIterator(object):
	def __init__(self, root):
		self.st = []
		self.pushLeft(root)

	def pushLeft(self, root):
		curr = root
		while curr:
			self.st.append(curr)
			curr = curr.left 

	def next(self):
		n = self.st.pop()
		self.pushLeft(n.right)
		return n

	def hasNext(self):
		return self.st

class Tree(object):
	def __init__(self, x):
	    self.val = x
	    self.left = None
	    self.right = None
        
r = Tree(1)
r.left = Tree(2)
r.right = Tree(3)
r.left.left = Tree(4)
r.left.right = Tree(5)
r.right.left = Tree(6)
r.right.right = Tree(7)

itr = TreeIterator(r)
while itr.hasNext():
	print itr.next().val,
print