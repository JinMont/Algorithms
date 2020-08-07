# Min Height BST

# ==============
# Before dive in
# ==============
# 1) Minimize the height of the BST
# 2) tha array is in sorted order and it can be useful to minimize the height
# 3) [1, 2, 5, 7, 10 ,13, 14, 15, 22]

# example 1)
# 1
#  \
#   2
#    \
#     5
#      \
#       ...
#  a) we don't want this since the height will be n which is not minimum

# example 2)
#     10
#    /  \
#   5    15
#  a) we can have the middle index of an array as the parent node
#  b) recursively have middle nodes of an left array and right array based on the node 10
#  c) we can achieve balanced log(n) height tree

# 4) we can have O(n) time by not using insert fuction(O(log(n)).
#  a) since we have the sorted array we can insert n nodes in n times
#  b) if we use insert fuction the time will be O(nlog(n))

def minHeightBst(array):
    return constructMinHeightBst(array, 0, len(array) - 1)

def constructMinHeightBst(array, startIdx, endIdx):
	if endIdx < startIdx:
		return None
	midIdx = (startIdx + endIdx) // 2
	bst = BST(array[midIdx])
	bst.left = constructMinHeightBst(array, startIdx, midIdx - 1)
	bst.right = constructMinHeightBst(array, midIdx + 1, endIdx)
	
	# If you want to use insert function that is O(nlog(n)) time
	# valueToAdd = array[midIdx]
	# if bst is None:
	# 	bst = BST(valueToAdd)
	# else:
	# 	bst.insert(valueToAdd)
	# constructMinHeightBst(array, bst, startIdx, midIdx - 1)
	# constructMinHeightBst(array, bst, midIdx + 1, endIdx)
	# return bst
	
	return bst
	
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
