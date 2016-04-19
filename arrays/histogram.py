def histogram(hist):
	maxArea = i = 0
	st = []
	while i < len(hist):
		if not st or hist[i] >= hist[st[-1]]:
			st.append(i)
			i += 1
		else:
			tp = st.pop()
			# after popping:
			# i-1 = rightmost index of elem > hist[tp], 
			# hist[tp] = smallest elem, 
			# st[-1]+1 is the leftmost index of elem > hist[tp]
			# width of rectangles = i - 1 - (st[-1] + 1) + 1 = i -1 - st[-1]
			area = hist[tp] * (i - 1 - st[-1] if st else i)
			maxArea = max(maxArea, area)
	print st
	while st:
		tp = st.pop()
		area = hist[tp] * (i - 1 - st[-1] if st else i)
		maxArea = max(maxArea, area)
	return maxArea

print histogram([6, 2, 5, 4, 5, 1, 6])