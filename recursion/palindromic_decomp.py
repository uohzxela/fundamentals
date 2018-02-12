def palin_decomp(s):
	decompose(s, [], 0, 0)

def is_palindromic(s, l, r):
	while l < r:
		if s[l] != s[r]:
			return False
		l += 1
		r -= 1
	return True

def decompose(s, decompositions, l, r):
	if r == len(s):
		if l == r:
			print decompositions
		return
	if is_palindromic(s, l, r):
		decompositions.append(s[l:r+1])
		decompose(s, decompositions, r+1, r+1)
		decompositions.pop()
	decompose(s, decompositions, l, r+1)


# palin_decomp("aab")
palin_decomp('0204451881')

# alternative solution
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.helper(s, 0, 1, [], res)
        return res
    
    def helper(self, s, start, end, partitions, res):
        if end >= len(s):
            if self.is_palin(s, start, end - 1):
                res.append(list(partitions) + [s[start:end]])
            return
        if self.is_palin(s, start, end - 1):
            partitions.append(s[start:end])
            self.helper(s, end, end + 1, partitions, res)
            partitions.pop()
        self.helper(s, start, end + 1, partitions, res)
        
    def is_palin(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        return True

