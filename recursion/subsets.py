'''
generate all subsets of size k from {1,2,3,...,n}
'''

def subsets(n, k):
    subsets_(n, k, 1, [])

def subsets_(n, k, s, partial):
    if len(partial) == k:
        print partial
        return
    for i in xrange(s, n+1):
        partial.append(i)
        subsets_(n, k, i+1, partial)
        partial.pop()


subsets(5, 3)