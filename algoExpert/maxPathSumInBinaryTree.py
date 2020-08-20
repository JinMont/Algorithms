# MPS(T):
#  LSB, LS = MPS(L)
#  RSB, RS = MPS(R)
#  MCSB = max(LSB, RSB) <= gives max of (Left Sum Branch and Right Sum Branch)
#  MSB = max(MCSB + V, V) <= max of (MCSB + Current Value and Current Value)
#  MST = max(MSB, LSB + V + RSB)
#  RMPS = max(LS, RS, MRT)
#  return (MSB, RMPS)

# findMaxSum gives two values
# 1) MSB => max value between its current value and its current value + max(left, right)
# 2) RMPS => max of ( LS, RS, MST )
#                      |
#             (MSB, LSB + V + RSB)
# 3) MSB is a max path of paths that can be used again
# 4) RMPS is a max path of paths that can be used again or not

def maxPathSum(tree):
    _, maxSum = findMaxSum(tree)
	return maxSum

def findMaxSum(tree):
	if tree is None:
		return (0, float("-inf"))
	
	leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
	rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
	maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)
	
	value = tree.value
	maxSumAsBranch = max(maxChildSumAsBranch + value, value)
	maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch)
	maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)
	
	return (maxSumAsBranch, maxPathSum)