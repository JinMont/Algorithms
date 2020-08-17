# Zigzag Traverse

# ==============
# Before dive in
# ==============
# 1) need to be able to see the pattern
# 2) pattern - only two direction of traversing
#  a) Down or Up
#   i) diagonally down
#    (1) at the end, go down
#  ii) diagonally up
#    (1) at the end, go to right

# [[0,1], [0,2], [0,3], [0,4]]
# [[1,1], [1,2], [1,3], [1,4]]
# [[2,1], [2,2], [2,3], [2,4]]
# [[3,1], [3,2], [3,3], [3,4]]

def zigzagTraverse(array):
	height = len(array) - 1
	width = len(array[0]) - 1
	result = []
	row, col = 0, 0
	# starting with goingDown so the position moves down for the first move
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
				# Time to go up
				# 1) when the position is on either row == height or col == 0
				if row == height:
					col += 1
				else:
					row += 1
			# if the position is not at the left end and then keep going down
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