# Same BSTs

# ==============
# Before dive in
# ==============
# 1) the first value must be same since it is the root node
# 2) the length of the two arrays must be same
# 3) Don't Construct the Actual BST to Compare <= too easy
# 4) if the length of the two arrays are 0 they are same

# ====
# Flow
# ====
# 1) check the first node of the two arrays are same
# 2) get the left and right nodes of each node 
#    (left is less than the root and vice versa)
# 3) compare recursively whether each node's left and right nodes are same in both arrays

# ====
# Time
# ====
# 1) computing O(n) + O(n) for each node
# 2) there are n nodes so O(n^2)

# =====
# Space
# =====
# 1) making n spaces for n nodes
# 2) therefor, O(n^2) for space as well
# 3) you can improve the space by O(n) but codes are more complicated

def sameBsts(arrayOne, arrayTwo):
	# length of two arrays must be same
    if len(arrayOne) != len(arrayTwo):
		return False
	# if length of two arrays is 0 then they are same
	if len(arrayOne) == 0 and len(arrayTwo) == 0:
		return True
	# the first element of the two arrays must be same since it is the root node
	# this part will recursively check subarrays
	if arrayOne[0] != arrayTwo[0]:
		return False
	
	leftOne = getSmaller(arrayOne)
	leftTwo = getSmaller(arrayTwo)
	rightOne = getBiggerOrEqual(arrayOne)
	rightTwo = getBiggerOrEqual(arrayTwo)
	
	return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)

def getSmaller(array):
	smaller = []
	for i in range(1, len(array)):
		if array[i] < array[0]:
			smaller.append(array[i])
	return smaller

def getBiggerOrEqual(array):
	biggerOrEqual = []
	for i in range(1, len(array)):
		if array[i] >= array[0]:
			biggerOrEqual.append(array[i])
	return biggerOrEqual