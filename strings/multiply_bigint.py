def multiply(a, b):
    a = list(a)
    b = list(b)
    a.reverse()
    b.reverse()

    res = [0] * (len(a) + len(b))
    for i in xrange(len(a)):
        for j in xrange(len(b)):
            res[i+j] += int(a[i]) * int(b[j])
            res[i+j+1] += res[i+j]/10
            res[i+j] %= 10

    if res[-1] == 0:
        res = res[:-1]
    res.reverse()
    return "".join([str(x) for x in res])

assert multiply("99", "99") == "9801"
assert multiply("1234567890123341232423424242", "3487827478787492894719841") == "4305959811600887801138200190763846741811246477785522"