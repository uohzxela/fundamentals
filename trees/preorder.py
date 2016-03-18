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

def preorder(root):
	if not root: return
	print root.val,
	preorder(root.left)
	preorder(root.right)

preorder(r)
print

def preorder_iter(root):
	s = [root]
	while s:
		r = s.pop()
		print r.val,
		if r.right: s.append(r.right)
		if r.left: s.append(r.left)
	print

preorder_iter(r)