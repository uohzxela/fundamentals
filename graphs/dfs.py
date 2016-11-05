g2 = {
    0 : [1,2,3],
    1 : [4,5],
    2 : [],
    3 : [],
    4 : [],
    5 : []
}

def dfs(g):
    visited = set()
    for v in g:
        if v in visited:
            continue
        dfs_(g, v, visited)

def dfs_(g, v, visited):
    visited.add(v)
    print v,
    for n in g[v]:
        if n in visited:
            continue
        dfs_(g, n, visited)
    
dfs(g2)