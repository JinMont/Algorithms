# Water Area

# Before dive in
# 1) know the tallest pillar left and right at an index
# 2) check the minimum height of the left and right pillars
# 3) water stores as much as the minimum height of step 2) - height at an index
#  a) tallest left   [0, 0, 8, 8, 8, 8, 8, 8, 10, 10, 10, 10, 10, 10]
#  b) tallest right  [10, 10, 10, 10, 10, 10, 10, 3, 3, 3, 3, 3, 3, 0]
#  c) current height [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
#  d) water stored   [0, 0, 8, 8, 3, 8, 8, 0, 3, 3, 2, 2, 3, 0] => sums up to 48
# 4) water stored calculation:
# if height < minHeight:
#  w = minHeight - height
# else:
#  w = 0

# Time
# 1) n time to find tallest left
# 2) n time to find tallest right
# 3) n time to calculate water stored at each index
# 4) 3n so O(n)

# Space
# 1) each array has length n 
# 2) O(n)

def waterArea(heights):
    maxes = [0 for x in heights]
	leftMax = 0
	
	for i in range(len(heights)):
		height = heights[i]
		maxes[i] = leftMax
		leftMax = max(leftMax, height)
	rightMax = 0
	for i in reversed(range(len(heights))):
		height = heights[i]
		minHeight = min(rightMax, maxes[i])
		# Calculate water level at the i
		if height < minHeight:
			maxes[i] = minHeight - height
		else:
			maxes[i] = 0
		# get new rightMax
		rightMax = max(rightMax, height)
	return sum(maxes)