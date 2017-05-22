# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraphDFS(self, node):
        if not node:
            return None
        vmap = {node.label: UndirectedGraphNode(node.label)}
        self.dfs(node, vmap)
        return vmap[node.label]
    
    def cloneGraphBFS(self, node):
        if not node:
            return None
        vmap = {node.label: UndirectedGraphNode(node.label)}
        first = node

        q = collections.deque([node])
        while q:
            node = q.popleft()
            for n in node.neighbors:
                if n.label not in vmap:
                    vmap[n.label] = UndirectedGraphNode(n.label)
                    q.append(n)
                vmap[node.label].neighbors.append(vmap[n.label])
        return vmap[first.label]
        
    def dfs(self, node, vmap):
        for n in node.neighbors:
            if n.label not in vmap:
                vmap[n.label] = UndirectedGraphNode(n.label)
                self.dfs(n, vmap)
            vmap[node.label].neighbors.append(vmap[n.label])
