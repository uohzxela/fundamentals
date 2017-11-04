def mergesort(A):
    if len(A) <= 1:
        return A

    m = len(A)/2
    left = mergesort(A[:m])
    right = mergesort(A[m:])

    return merge(left, right)


def merge(left, right):
    res = []
    p1 = p2 = 0

    while p1 < len(left) and p2 < len(right):
        if left[p1] <= right[p2]:
            res.append(left[p1])
            p1 += 1
        else:
            res.append(right[p2])
            p2 += 1

    res += left[p1:]
    res += right[p2:]

    return res

assert mergesort([23, 21, 5, 9, 10, 4, 1, 8, 3, 0, -1, -10]) == sorted([23, 21, 5, 9, 10, 4, 1, 8, 3, 0, -1, -10])
