def max_profit(prices):
	min_price = float('inf')
	max_profit = 0

	for p in prices:
		max_profit = max(max_profit, p - min_price)
		min_price = min(min_price, p)

	return max_profit

assert max_profit([310,315,275,295,260,270,290,230,255,250]) == 30
