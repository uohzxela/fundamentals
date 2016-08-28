
from collections import defaultdict
g = {
    0 : [1,2],
    1: [2],
    2: [0,3],
    3: [3],
}

g2 = {
    0 : [1,2,3],
    1 : [],
    2 : [],
    3 : []
}

def has_cycle(g):
    alive = defaultdict(lambda: None)
    visited = defaultdict(lambda: None)
    for v in g:
        if not visited[v] and has_cycle_(g, v, alive, visited): 
            return True
    return False

def has_cycle_(g, v, alive, visited):
    alive[v] = True
    visited[v] = True
    for n in g[v]:
        if visited[n] and alive[n]:
            return True
        elif not visited[n] and has_cycle_(g, n, alive, visited):
            return True
    alive[v] = False
    return False
    
assert has_cycle(g) 
assert not has_cycle(g2)