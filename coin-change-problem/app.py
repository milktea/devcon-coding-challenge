from itertools import product

def coinChange(change, coins):
	"""
	one liner coin change 

	"""
	return set([tuple(sorted(x)) for i in xrange(1, change+1) for x in set(product(coins, repeat=i)) if sum(x) == change])



#tests
coins = [1, 2, 3]
change = 4
print coinChange(change, coins)

coins = [2, 5, 3, 6]
change = 10
print coinChange(change, coins)