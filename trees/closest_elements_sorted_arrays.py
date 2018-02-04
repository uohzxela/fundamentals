import bintrees

def find_closest_elements_in_sorted_arrays(sorted_arrays):
	min_dist_so_far = float('inf')
	iters = bintrees.RBTree()
	for idx, array in enumerate(sorted_arrays):
		it = iter(array)
		first_min = next(it, None)
		if first_min:
			# first_min is inserted with idx as tuple
			# to differentiate duplicate elements among sorted arrays
			iters.insert((first_min, idx), it)

	while True:
		print_tree(iters)
		min_value, min_idx = iters.min_key()
		max_value = iters.max_key()[0]
		min_dist_so_far = min(max_value - min_value, min_dist_so_far)
		it = iters.pop_min()[1]
		next_min = next(it, None)
		if next_min is None:
			return min_dist_so_far
		# next_min is inserted with min_idx as tuple
		# to differentiate duplicate elements among sorted arrays
		iters.insert((next_min, min_idx), it)

def print_tree(tree):
	for key in tree.keys():
		print key,
	print

sorted_arrays = [[5,10,15],[3,6,9,12,15],[8,16,24]]
assert find_closest_elements_in_sorted_arrays(sorted_arrays) == 1
