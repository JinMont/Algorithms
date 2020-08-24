# Min Number of Jumps

# Before dive in
# 1) Dynamic programming 
# 2) make another array jumps that has same length as input array
# 3) when we have i and j check whether i can be reached from j (array[j] + j)
# 4) if array[j] + j >= i:                    <= i = 1, j = 0, 3+0=4 >= 1:
# 5)   jumps[i] = min(jumps[i], jumps[j] + 1) <= jumps[1] = min(inf, 0+1)


# array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
# jumps = [0, 1, 1, 1, 2, 2, 3, inf, inf, inf, 4]
# output 4 // 3 --> (4 or 2) --> (2 or 3) --> 7 --> 3

# Time 
# O(n^2)

# Space
# O(n)

def minNumberOfJumps(array):
	jumps = [float("inf") for x in array]
	jumps[0] = 0
	for i in range(1, len(array)):
		for j in range(0, i):
			# can i be reached from j with the steps in j
			if array[j] >= i - j:
				# the elements that are in range of left most element's jump will have same jump value
				jumps[i] = min(jumps[j] + 1, jumps[i])
	return jumps[-1]

# Little more clever solution
# Time O(n) | O(1) space
def minNumberOfJumps(array):
	if len(array) == 1:
		return 0
	jumps = 0
	maxReach = array[0]
	steps = array[0]
	# between 1 ~ len(array) - 1
	for i in range(1, len(array) - 1):
		# as i increments calculate new maxReach
		maxReach = max(maxReach, i + array[i])
		# we also decrements steps we have
		steps -= 1
		# when we have 0 steps we increment jump and get new steps
		# based on the maxReach we have and the current i position
		# maxReach - i means how many steps we have
		if steps == 0:
			jumps += 1
			steps = maxReach - i
	# retrun the jumps + 1
	# why + 1? because we didn't make the last jump yet
	return jumps + 1