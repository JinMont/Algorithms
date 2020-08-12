# Four Number Sum

# ==============
# Before dive in
# ==============
# 1) we don't want O(n^4) time
# 2) Pair two numbers and add its sum in a hash table 
# 3) there can be more than one pair for the exact same sum
#  a) store them in an array [[4, 2], [-1, 7]]
# 4) Avoid double count (duplicate)
#  a) [7, 6] and [7, -1] have the duplicate 7
#  b) partition input array with the current position of the loop
#  c) [         part A hash table         ]|[            part B           ]
#  c) [elements that are in the hash table]|[elements that haven't reached]
#  d) pick a pair of two elements in part A and part B for the target sum
# 5) Add the quadruplet only when there is (target - part B pair sum) in the hash table of part A
#  a) it can prevent making duplicates of quadruplets
#  b) [7, 6, -1 , 4], [ -1, 6, 7, 4] We want only one of them

# ====
# Time
# ====
# 1) Average Case: O(n^2)
#  a) [      n elements      ] - n 
#  b) [part A - n][part B - n] - 2n  
#  c) n*2n = 2n^2 drop the constant so O(n^2)
# 2) Worst Case: O(n^3)
#  a) when loop through all the elements in the hash table
#  b) that is another n times

# =====
# Space
# =====
# 1) O(n^2) since n element pair n times
def fourNumberSum(array, targetSum):
    allPairSums = {}
	quadruplets = []
	for i in range(1, len(array) - 1):
		for j in range(i + 1, len(array)):
			currentSum = array[i] + array[j]
			difference = targetSum - currentSum
			if difference in allPairSums:
				for pair in allPairSums[difference]:
					quadruplets.append(pair + [array[i], array[j]])
		# After summing a pair in part B and finding the difference in part A hash table
		# make new pairs with index i to add them in the part A hash table
		for k in range(0, i):
			currentSum = array[i] + array[k]
			if currentSum not in allPairSums:
				allPairSums[currentSum] = [[array[k], array[i]]]
			else:
				allPairSums[currentSum].append([array[k], array[i]])
	return quadruplets