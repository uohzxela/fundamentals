def printInterleaves_(s1, s2, i, j, s3):
	if i > len(s1)-1:
		print s3 + s2[j:]
		return
	if j > len(s2)-1:
		print s3 + s1[i:]
		return
	printInterleaves_(s1, s2, i+1, j,  s3 + s1[i])
	printInterleaves_(s1, s2, i, j+1, s3 + s2[j])


def printInterleaves(s1, s2):
	print printInterleaves_(s1, s2, 0, 0, "")

printInterleaves("AB", "CD")