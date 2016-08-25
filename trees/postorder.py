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

# Space complexity: O(n)
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

"""
1.1 Create an empty stack
2.1 Do following while root is not NULL
    a) Push root's right child and then root to stack.
    b) Set root as root's left child.
2.2 Pop an item from stack and set it as root.
    a) If the popped item has a right child and the right child 
       is at top of stack, then remove the right child from stack,
       push the root back and set root as root's right child.
    b) Else print root's data and set root as NULL.
2.3 Repeat steps 2.1 and 2.2 while stack is not empty.
"""
# Space complexity: O(1)
def postorder_iter2(root):
	st = []
	while root or st:
		while root:
			if root.right:
				st.append(root.right)
			st.append(root)
			root = root.left
		root = st.pop()
		if st and root.right == st[-1]:
			st.pop()
			st.append(root)
			root = root.right
		else:
			print root.val,
			root = None
	print

postorder_iter(r)
postorder_iter2(r)