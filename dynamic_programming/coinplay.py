from collections import deque
def coinplay(coins):
	return coinplay_(deque(coins), 0, 0)

def coinplay_(coins, i, res):
	if not coins: return res
	if i % 2 == 0:
		c = coins.popleft()
		res1 = coinplay_(coins, i+1, res + c)
		coins.appendleft(c)
		c = coins.pop()
		res2 = coinplay_(coins, i+1, res + c) 
		coins.append(c)
		return max(res1, res2)
	else:
		c = coins.popleft()
		res1 = coinplay_(coins, i+1, res) 
		coins.appendleft(c)
		c = coins.pop()
		res2 = coinplay_(coins, i+1, res) 
		coins.append(c)
		return min(res1, res2)

print coinplay([8,15,3,7])
print coinplay([2,2,2,2])
print coinplay([20, 30, 2, 2, 2, 10])
