import collections

# EPI version
def longest_subarray_with_distinct_entries(A):
	latest_occurrence = {}
	longest_dup_free_subarray_start_idx = res = 0

	for i, a in enumerate(A):
		if a in latest_occurrence:
			dup_idx = latest_occurrence[a]
			if dup_idx >= longest_dup_free_subarray_start_idx:
				res = max(res, i - longest_dup_free_subarray_start_idx)
				longest_dup_free_subarray_start_idx = dup_idx + 1
		latest_occurrence[a] = i
	return res

# my version - two pointers
def longest_subarray_with_distinct_entries2(A):
	left = res = 0
	entry_freq = collections.Counter()
	for right, entry in enumerate(A):
		entry_freq[entry] += 1
		while entry_freq[entry] > 1:
			entry_freq[A[left]] -= 1
			left += 1
		res = max(right - left + 1, res)
	return res

assert longest_subarray_with_distinct_entries(['f', 's', 'f', 'e', 't', 'w', 'e', 'n', 'w', 'e']) == 5
assert longest_subarray_with_distinct_entries2(['f', 's', 'f', 'e', 't', 'w', 'e', 'n', 'w', 'e']) == 5
assert longest_subarray_with_distinct_entries2(['a', 's','d', 'f', 'f']) == 4
