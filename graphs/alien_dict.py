from collections import defaultdict
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        g = {}
        n = len(words)
        self.createVertices(g, words)
        for i in xrange(n-1):
            self.insertOrder(g, words[i], words[i+1])
        if len(g) == 0: g[words[0][0]] = []
        return "".join(self.toposort(g))

    def createVertices(self, g, words):
        uniqueChars = set(''.join(words))
        for c in uniqueChars: g[c] = []
        
    def insertOrder(self, g, s1, s2):
        p1 = p2 = 0
        while p1 < len(s1) and p2 < len(s2):
            if s1[p1] != s2[p2]:
                if s2[p2] not in g[s1[p1]]:
                    g[s1[p1]].append(s2[p2])
                return
            p1 += 1
            p2 += 1
            
    def toposort(self, g):
        stack = []
        visited = defaultdict(lambda: None)
        alive = defaultdict(lambda: None)
        for v in g:
            if not visited[v] and self.toposort_(g, v, visited, stack, alive):
                return []
        return reversed(stack)
        
    def toposort_(self, g, v, visited, stack, alive):
        visited[v] = True
        alive[v] = True
        for n in g[v]:
            if not visited[n] and self.toposort_(g, n, visited, stack, alive):
                return True
            elif visited[n] and alive[n]:
                return True
        alive[v] = False
        stack.append(v)
        return False