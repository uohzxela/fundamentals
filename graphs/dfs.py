from collections import defaultdict

g2 = {
    0 : [1,2,3],
    1 : [4,5],
    2 : [],
    3 : [],
    4 : [],
    5 : []
}

def dfs(g):
    visited = defaultdict(lambda: None)
    for v in g:
        if not visited[v]: 
            dfs_(g, v, visited)

def dfs_(g, v, visited):
    visited[v] = True
    print v,
    for n in g[v]:
        if not visited[n]:
            dfs_(g, n, visited)
    
dfs(g2)