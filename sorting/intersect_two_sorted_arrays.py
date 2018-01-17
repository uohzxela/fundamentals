def intersect(A1, A2):
	p1, p2, intersection = 0, 0, []
	while p1 < len(A1) and p2 < len(A2):
		if A1[p1] == A2[p2]:
			if not intersection or intersection[-1] != A1[p1]:
				intersection.append(A1[p1])
			p1, p2 = p1 + 1, p2 + 1
		elif A1[p1] < A2[p2]:
			p1 += 1
		else:
			p2 += 1
	return intersection

assert intersect([2,3,3,5,7,11], [3,3,7,15,31]) == [3, 7]
