'''
generate all subsets of size k from {1,2,3,...,n}
'''

def subsets(n, k):
    subsets_(n, k, 1, [])
'''
optimized version
'''
# def subsets_(n, k, p, curr):
#     if len(curr) == k:
#         print curr
#         return
#     remaining = k-len(curr)
#     i = p
#     while i <= n and remaining <= (n - i  + 1):
#         curr.append(i)
#         subsets_(n, k, i+1, curr)
#         curr.pop()
#         i += 1

def subsets_(n, k, p, curr):
    if len(curr) == k:
        print curr
        return
    for i in xrange(p, n+1):
        curr.append(i)
        subsets_(n, k, i+1, curr)
        curr.pop()


subsets(5, 3)