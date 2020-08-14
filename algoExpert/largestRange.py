# Largest Range

# ==============
# Before dive in
# ==============
# 1) Find the largest range of intergers in the input array
# Example)
#  a) [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
#  b) the largest range of contiguous integers among elements of the input array is [0, 7]
# 2) In the first, you might think of using sorting the array in O(nlog(n)) but you can do faster
# 3) Store all the numbers in the hash table

def largestRange(array):
    bestRange = []
	longestLength = 0
	nums = {}
	for num in array:
		nums[num] = True
	for num in array:
		# if the number isn't true
		if not nums[num]:
			continue
		nums[num] = False
		currentLength = 1
		left = num - 1
		right = num + 1
		while left in nums:
			nums[left] = False
			currentLength += 1
			left -= 1
		while right in nums:
			nums[right] = False
			currentLength += 1
			right += 1
		if currentLength > longestLength:
			longestLength = currentLength
			bestRange = [left + 1, right - 1]
			# the best range is left before -=1 and right before += 1
	return bestRange
