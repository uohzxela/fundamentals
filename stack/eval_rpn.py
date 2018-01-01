class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        OPERATORS = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            # need to use float() for x to pass Leetcode, e.g. int(6 / -132) gives -1 but int(float(6) / -132) gives 0
            '/': lambda y, x: int(float(x) / y)
        }
        st = []
        for token in tokens:
            if token in OPERATORS:
                st.append(OPERATORS[token](st.pop(), st.pop()))
            else:
                st.append(int(token))
        return st[-1]
