from ..trees.utils import printTree, TreeNode

# cd one level up fundamentals directory and python -m fundamentals.recursion.generate_binary_trees

def generate_binary_trees(num_nodes):
	if num_nodes == 0:
		return [None]
	res = []
	for left_num_nodes in xrange(num_nodes):
		right_num_nodes = num_nodes - 1 - left_num_nodes
		left_subtrees = generate_binary_trees(left_num_nodes)
		right_subtrees = generate_binary_trees(right_num_nodes)
		res += [TreeNode(0, left, right) for left in left_subtrees for right in right_subtrees]
	return res

def test(num_nodes):
	trees = generate_binary_trees(num_nodes)
	print 'Testing ' + str(num_nodes) + ' nodes:'
	for tree in trees:
		printTree(tree)
		print '-----------------'

test(3)
test(4)
