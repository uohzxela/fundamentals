def alternate(A):
    negIndex = posIndex = 0
    for i in xrange(len(A)):
        if i % 2 == 0 and A[i] >= 0:
            negIndex = findNegIndex(A, i+1)
            if negIndex >= len(A): return A
            neg = A[negIndex]
            rotate(A, i, negIndex-1)
            A[i] = neg
        elif i%2 == 1 and A[i] < 0:
            posIndex = findPosIndex(A, i+1)
            if posIndex >= len(A): return A
            pos = A[posIndex]
            rotate(A, i, posIndex-1)
            A[i] = pos
    return A

def findPosIndex(A, i):
    for i in xrange(i,len(A)):
        if A[i] >= 0: return i
    return len(A)

def findNegIndex(A, i):
    for i in xrange(i,len(A)):
        if A[i] < 0: return i
    return len(A)

def rotate(A, s, e):
    prev = A[s]
    for i in xrange(s+1, e+2):
        curr = A[i]
        A[i] = prev
        prev = curr


print alternate([2,3,-4,-9,-1,-7,1,-5,-6,-10,-9])