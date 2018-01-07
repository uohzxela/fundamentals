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

# only works for perfect binary trees
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

# generic solution that also works for general binary trees
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        dummy = child = TreeLinkNode(0)
        while root:
            child.next = root.left
            if child.next:
                child = child.next
            child.next = root.right
            if child.next:
                child = child.next
            if root.next:
                root = root.next
            else:
                root = dummy.next
                child = dummy
