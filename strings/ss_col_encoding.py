def ss_col_encode(col):
	res = 0
	for c in col:
		res = res * 26 + ord(c) - ord('A') + 1
	return res

assert ss_col_encode('AA') == 27
assert ss_col_encode('AB') == 28
assert ss_col_encode('ZZ') == 702
assert ss_col_encode('A') == 1
assert ss_col_encode('Z') == 26
