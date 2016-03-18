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

def postorder(root):
	if not root: return
	postorder(root.left)
	postorder(root.right)
	print root.val,

postorder(r)
print

def postorder_iter(root):
	s1 = [root]
	s2 = []
	while s1:
		r = s1.pop()
		s2.append(r)
		if r.left: s1.append(r.left)
		if r.right: s1.append(r.right)
	while s2:
		print s2.pop().val,
	print

postorder_iter(r)