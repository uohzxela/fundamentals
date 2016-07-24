def buy_sell_twice(prices):
	first_buy_sell_profits = []
	min_price = float("inf")
	max_profit = 0

	for i in xrange(len(prices)):
		min_price = min(min_price, prices[i])
		max_profit = max(max_profit, prices[i] - min_price)
		first_buy_sell_profits.append(max_profit)

	max_price = float("-inf")

	for i in xrange(len(prices)-1, 0, -1):
		max_price = max(max_price, prices[i])
		max_profit = max(max_profit, max_price - prices[i] + first_buy_sell_profits[i-1])

	return max_profit

assert buy_sell_twice([12,11,13,9,12,8,14,13,15]) == 10