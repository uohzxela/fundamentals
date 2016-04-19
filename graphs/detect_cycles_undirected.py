def has_cycle(g):
    visited = defaultdict(lambda: None)
    for v in g:
        if not visited[v] and has_cycle_(g, v, visited, None): 
            return True
    return False

def has_cycle_(g, v, visited, parent):
    visited[v] = True
    for n in g[v]:
        if not visited[n] and has_cycle_(g, n, visited, v): return True
        elif visited[n] and n != parent: return True
    return False
    