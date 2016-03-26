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

#      1
#   2     3
# 4  5   6  7

def inorder(root):
	if not root: return 
	inorder(root.left)
	print root.val,
	inorder(root.right)


inorder(r)
print

def inorder_iter(root):
	st = []
	curr = root
	while st or curr:
		while curr:
			st.append(curr)
			curr = curr.left
		n = st.pop()
		print n.val,
		curr = n.right
	print

inorder_iter(r)