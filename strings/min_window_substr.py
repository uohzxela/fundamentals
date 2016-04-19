
def  MinWindow( s,  t):
    if len(t) > len(s): return ""
    tCounter, sCounter = defaultdict(int), defaultdict(int)
    res = ""
    minLen = float('inf')
    left = count = 0
    
    for c in t: tCounter[c] += 1
    
    for i in xrange(len(s)):
        c = s[i]
        # curr index is the right index
        # keep adding elements to sCounter if it's in tCounter
        # increase count of elems added (only if it's not redundant) 
        # until it fulfils the condition (count == len(t))
        if c in tCounter:
            if sCounter[c] < tCounter[c]:
                count += 1
            sCounter[c] += 1
    
        if count == len(t):
            sc = s[left]
            # shrink window while maintaining the condition, by removing extra or invalid chars from the left
            while sc not in sCounter or sCounter[sc] > tCounter[sc]:
                if sc in sCounter and sCounter[sc] > tCounter[sc]:
                    sCounter[sc]  -= 1
                left += 1
                sc = s[left]
            if i - left + 1 < minLen:
                res = s[left: i+1]
                minLen = i - left + 1
    return res
