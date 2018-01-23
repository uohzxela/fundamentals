def find_k_largest_in_bst(root, k):
	res = []
	helper(root, k, res)
	return res

def helper(root, k, res):
	if not root:
		return
	if len(res) < k:
		helper(root.right, k, res)
		if len(res) < k:
			res.append(root.val)
			helper(root.left, k, res)
