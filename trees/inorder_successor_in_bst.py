def inorder_successor(root, target, parent=None):
	if not root:
		return
	if target.val == root.val:
		if not target.right:
			return parent
		curr = target.right
		while curr.left:
			curr = curr.left
		return curr
	elif target.val < root.val:
		return inorder_successor(root.left, target, root)
	else:
		return inorder_successor(root.right, target, root)

def inorder_successor(root, k):
	successor = None
	while root:
		if root.val > k:
			successor = root
			root = root.left
		else:
			root = root.right
	return successor.val
