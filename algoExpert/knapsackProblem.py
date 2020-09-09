# Example
# =======
#        0 1 2 3 4 5 6 7 8 9 10 <- capacity
# [ ]    0 0 0 0 0 0 0 0 0 0 0
# [1, 2] 0 0 1 1 1 1 1 1 1 1 1
# [4, 3] 0 0 1 4 4 5 5 5 5 5 5
# [5, 6] 0 0 1 4 4 5 5 5 6 9 9 
# [6, 7] 0 0 1 4 4 5 5 6 6 7 10
#   ^ items

def knapsackProblem(items, capacity):
    knapsackValues = [[0 for x in range(0, capacity + 1)] for y in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
    	currentWeight = items[i - 1][1]
    	currentValue = items[i - 1][0]
    	for c in range(0, capacity + 1):
    		if currentWeight > c:
    			# if the current weight is bigger than the capacity
    			knapsackValues[i][c] = knapsackValues[i - 1][c]
    			# bring the value from above
    		else:
    			# compute max of
    			# 1) value above
    			# 2) previous item's value + current value
    			knapsackValues[i][c] = max(
    				knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue
    			)
    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]

def getKnapsackItems(knapsackValues, items):
	sequence = []
	i = len(knapsackValues) - 1 # items ex) 4 items knapsackValue has +1 len
	c = len(knapsackValues[0]) - 1 # capacity ex) 10 caps
	while i > 0:
		if knapsackValues[i][c] == knapsackValues[i - 1][c]:
			i -= 1
		else:
			sequence.append(i - 1) # append i - 1 because it needs the index
			c -= items[i - 1][1] # reduce the cap from c
			i -= 1 # reduce the num of items
		if c == 0: # when there is no more cap left break
			break
	return list(reversed(sequence)) # reverse to show items in order