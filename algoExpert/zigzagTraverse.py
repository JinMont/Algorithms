# Before dive in
# ==============
# 1) need to be able to see the pattern

# [[0,1], [0,2], [0,3], [0,4]]
# [[1,1], [1,2], [1,3], [1,4]]
# [[2,1], [2,2], [2,3], [2,4]]
# [[3,1], [3,2], [3,3], [3,4]]

# 0,0 1,0 0,1 0,2 1,1 2,0 

# 3,0 2,1 1,2 0,3 

# 1,3 2,2 3,1 3,2 2,3 3,3

def zigzagTraverse(array):
	height = len(array) - 1
	width = len(array[0]) - 1
	result = []
	row, col = 0, 0
	goingDown = True
	while not isOutOfBounds(row, col, height, width):
		result.append(array[row][col])
		if goingDown:
			# when column is at 0 or row is at the end of the rows
			# [o, -, -, -]
			# [o, -, -, -]
			# [o, -, -, -]
			# [o, o, o, o]
			if col == 0 or row == height:
				goingDown = False
				if row == height:
					col += 1
				else:
					row += 1
			else:
				row += 1
				col -= 1
		else:
			if row == 0 or col == width:
				goingDown = True
				if col == width:
					row += 1
				else:
					col += 1
			else:
				row -= 1
				col += 1
	return result
			
def isOutOfBounds(row, col, height, width):
	return row < 0 or row > height or col < 0 or col > width