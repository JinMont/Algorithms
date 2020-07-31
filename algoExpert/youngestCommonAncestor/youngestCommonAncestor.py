# This repository is only for the personal educational purpose.
# The code below is from algoExpert.

# Youngest Common Ancestor
# ====
# Flow
# ====
# 1) find the depth of two descendants
# 2) compare the depth of both and increase the height of the lower element up to the height of the higher descendant
# 3) loop until both descendants find the common ancestor
# 4) each loop makes the descendants find their ancestors until both have the same ancestor

# ==============
# Time and Space
# ==============
# Time: O(d) time where d is the depth of the ancestral tree
# 1) Since the descedants need to move only d times to find the common ancestor
#   a) I think if the tree is not balanced it takes O(n) where n is the number of descendants and if it is balanced it takes O(log(n)) where n is the number of descendants in the tree. 
# Space: O(1) space
# 1) need only constant space

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
    	return climbAncestry(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
    	return climbAncestry(descendantTwo, descendantOne, depthTwo - depthOne)

def getDescendantDepth(descendant, topAncestor):
	depth = 0
	while descendant != topAncestor:
		depth += 1
		descendant = descendant.ancestor
	return depth

def climbAncestry(lowerDescendant, higherDescendant, diff):
	while diff > 0:
		lowerDescendant = lowerDescendant.ancestor
		diff -= 1
	while lowerDescendant != higherDescendant:
		lowerDescendant = lowerDescendant.ancestor
		higherDescendant = higherDescendant.ancestor
	return lowerDescendant



