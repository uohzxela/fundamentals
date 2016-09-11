def multiply(a, b):
    a = list(a)
    b = list(b)
    a.reverse()
    b.reverse()
    res = [0] * (len(a) + len(b))
    for b_i in xrange(len(b)):
        carry = 0
        for a_i in xrange(len(a)):
            res[a_i + b_i] += carry + int(a[a_i]) * int(b[b_i])
            carry = res[a_i + b_i] / 10
            res[a_i + b_i] = res[a_i + b_i] % 10
        res[b_i + len(a)] += carry
    res = res[:-1]
    res.reverse()
    return "".join([str(x) for x in res])