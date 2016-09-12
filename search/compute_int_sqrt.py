def sqrt(x):
    left, right = 0, x
    while left <= right:
        mid = (left + right)/2
        if mid*mid <= x:
            left = mid + 1
        else:
            right = mid - 1
    # why minus 1? because left = mid + 1,
    # we need to get the most recent mid
    return left - 1

assert sqrt(0) == 0
assert sqrt(1) == 1
assert sqrt(4) == 2
assert sqrt(9) == 3
assert sqrt(300) == 17
assert sqrt(25) == 5