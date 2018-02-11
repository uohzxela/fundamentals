def generate_matched_parens(n):
	res = []
	generate("", n, n, res)
	return res

def generate(s, left, right, res):
	if left == 0 and right == 0:
		res.append(s)
		return
	if left > 0:
		generate(s + "(", left-1, right, res)
	if left < right:
		generate(s + ")", left, right-1, res)

print generate_matched_parens(4)

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(partial, res, mismatched_count, n):
            if mismatched_count < 0:
                return
            if len(partial) == n * 2:
                if mismatched_count == 0:
                    res.append(partial)
                return
            helper(partial + '(', res, mismatched_count + 1, n)
            helper(partial + ')', res, mismatched_count - 1, n)
        
        res = []
        helper('', res, 0, n)
        return res
