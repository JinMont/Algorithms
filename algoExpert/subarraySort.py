# ==============
# Before dive in
# ==============
# Example) 
# [         <--need to be sorted-->           ]
# [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
# [                    <-not this->           ]
# index 3 to 9 need to be sorted so output is: [3, 9]

# ====
# Flow
# ====
# 1) find the unsorted subarray
# 2) find the smallest number in the subarray and find its position in the final array
#  a) 6 is the smallest of the unsorted subarray and its position is in between index 2 and 3
# 3) find the biggest number in the subarray and find its position in the final array
#  b) 12, between 9 and 10
# 4) if you sort elements between 3 and 9 all the elements are sorted

# =====
# Space
# =====
# everything happens in place so O(1)

# ====
# Time
# ====
# 1) O(n)
# 2) find the unsorted subarray which takes O(n)
# 3) and then find the position of the smallest and the biggest element of the subarray
#  a) which takes another O(n)
# 4) n + n = 2n and if you drop the constant it is O(n)

def subarraySort(array):
	# we are going to find the min and max of the unsorted subarray
    minOutOfOrder = float("inf")
	maxOutOfOrder = float("-inf")
	
	for i in range(len(array)):
		num = array[i]
		if isOutOfOrder(i, num, array):
			minOutOfOrder = min(minOutOfOrder, num)
			maxOutOfOrder = max(maxOutOfOrder, num)
	# when the min isn't changed the array is sorted
	if minOutOfOrder == float("inf"):
		return [-1, -1]
	# find and stop before the element bigger than the min
	subarrayLeftIdx = 0
	while minOutOfOrder >= array[subarrayLeftIdx]:
		subarrayLeftIdx += 1
	# find and stop before the lement bigger than the max
	subarrayRightIdx = len(array) - 1
	while maxOutOfOrder <= array[subarrayRightIdx]:
		subarrayRightIdx -= 1
	# return an index that shows the range of the unsorted array (inclusive)
	return [subarrayLeftIdx, subarrayRightIdx]

def isOutOfOrder(i, num, array):
	# when i is at index 0
	if i == 0:
		return num > array[i + 1]
	# when i is at the last index
	if i == len(array) - 1:
		return num < array[i - 1]
	# when i is in the middle of the array
	return num > array[i + 1] or num < array[i - 1]