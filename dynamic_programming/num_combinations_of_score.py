def num_combinations(play_scores, final_score):
	return num_combinations_(play_scores, final_score, len(play_scores)-1)

def num_combinations_(play_scores, final_score, i):
	if final_score == 0:
		return 1
	if final_score < 0 or i < 0:
		return 0
	num1 = num_combinations_(play_scores, final_score - play_scores[i], i)
	num2 = num_combinations_(play_scores, final_score, i-1)
	return num1 + num2

assert num_combinations([2, 3, 7], 12) == 4

def num_combinationsDP(play_scores, final_score):
	dp = [[0 for j in xrange(len(play_scores)+1)] for i in xrange(final_score+1)]
	for i in xrange(len(play_scores)+1):
		dp[0][i] = 1
	for final_score in xrange(1, final_score+1):
		for i in xrange(1, len(play_scores)+1):
			num = dp[final_score][i-1]
			new_final_score = final_score - play_scores[i-1]
			if new_final_score >= 0:
				num += dp[new_final_score][i]
			dp[final_score][i] = num
	return dp[-1][-1]

assert num_combinationsDP([2, 3, 7], 12) == 4
assert num_combinationsDP([2, 3, 7], 9) == 3