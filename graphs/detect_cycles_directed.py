
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
    for k, v in g.iteritems():
        if has_cycle_(g, k, alive, visited): 
            return True
    return False

def has_cycle_(g, v, alive, visited):
    if not visited[v]:
        alive[v] = True
        visited[v] = True
        for n in g[v]:
            if not visited[n] and has_cycle_(g, n, alive, visited): return True
            elif visited[n] and alive[n]: return True
    alive[v] = False
    return False
    
print has_cycle(g)
print has_cycle(g2)