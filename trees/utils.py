def printLevel(root):
	if not root: return
	q = [root]
	while q:
		curr_len = len(q)
		for _ in xrange(curr_len):
			n = q.pop(0)
			if n.left: q.append(n.left)
			if n.right: q.append(n.right)
			print n.val,
		print

def printList(curr):
	while curr:
		print curr.val,
		curr = curr.next
	print

def printTree(root):
	printTree_(root, "")

def printTree_(root, indent):
	if root:
		printTree_(root.right, indent + "    ")
		print indent + str(root.val)
		printTree_(root.left, indent + "    ")

def findLen(curr):
	count = 0
	while curr:
		count += 1
		curr = curr.next
	return count

