MAPPING = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

def phone_mnemonic(num):
	mnemonics = []
	phone_mnemonic_(num, [], mnemonics, 0)
	return mnemonics

def phone_mnemonic_(num, s, mnemonics, i):
	if i > len(num)-1:
		mnemonics.append("".join(s))
		return
	for c in MAPPING[int(num[i])]:
		s.append(c)
		phone_mnemonic_(num, s, mnemonics, i+1)
		s.pop()

assert "ACRONYM" in phone_mnemonic("2276696")
assert "ABPOMZN" in phone_mnemonic("2276696")
