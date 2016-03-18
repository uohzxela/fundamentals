def subsets(nums):

    table = [False for i in xrange(len(nums))]
    subsets_(nums, len(nums)-1, table)
    
def subsets_(nums, i, table):
    if i < 0:
    	for i,t in enumerate(table):
    		if t: print nums[i],
    	print
    	return
    table[i] = True
    subsets_(nums, i-1, table)
    table[i] = False
    subsets_(nums, i-1, table)

subsets([1,2,3])