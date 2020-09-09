#        0 1 2 3 4 5 6 7 8 9 10
# [ ]    0 0 0 0 0 0 0 0 0 0 0
# [1, 2] 0 0 1 1 1 1 1 1 1 1 1
# [4, 3] 0 0 1 4 4 5 5 5 5 5 5
# [5, 6] 0 0 1 4 4 5 5 5 6 9 9 
# [6, 7] 0 0 1 4 4 5 5 6 6 7 10

def knapsackProblem(items, capacity):
    knapsackValues = [[0 for x in range(0, capacity + 1)]]
    for i in range(1, len(items) + 1):
    	currentWeight = items[i - 1][1]
    	currentValue = items[i - 1][0]
    	for c in range(0, capacity + 1):
    		if currentWeight > c:
    			knapsackValues[i][c] = knapsackValues[i - 1][c]
    		else:
    			knapsackValues[i][c] = max(
    				knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue
    			)
    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]

def getKnapsackItems(knapsackValues, items):
	sequence = []
	i = len(knapsackValues) - 1
	c = len(knapsackValues[0]) - 1
	while i > 0:
		if knapsackValues[i][c] == knapsackValues[i - 1][c]:
			i -= 1
		else:
			sequence.append(i - 1)
			c -= items[i - 1][1]
			i -= 1
		if c == 0:
			break
	return list(reversed(sequence))