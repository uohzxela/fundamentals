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



def inorderIter(root):
	s, curr = [], root
	while s or curr:
		while curr:
			s.append(curr)
			curr = curr.left
		n = s.pop()
		print n.val,
		curr = n.right
	print

inorder(r)
print
inorderIter(r)