# Search In Sorted Matrix

# ==============
# Before dive in
# ==============
# 1) I think it was similar to Binary Search Tree in the idea that 
#    you can increase row or decrease column based on the comparision of target and current postition
# 2) Since the row and column are in sorted order, 
#    you want to start at the top right corner to use the advantage moving row and column
#  a) when you increase row => target > current position
#  b) when you decrease column => target < current position

def searchInSortedMatrix(matrix, target):
	row = 0
	col = len(matrix[0]) - 1
	while row < len(matrix) and col >= 0:
		if target == matrix[row][col]:
			return [row, col]
		elif target < matrix[row][col]:
			col -= 1
		else:
			row += 1
	return [-1, -1]