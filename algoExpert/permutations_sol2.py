# Permutations Solution 2

# =======
# Example
# =======
# array = [1, 2, 3]
# permHelper(i, array, permutations)

# => permHelper(0, [1, 2, 3], perm)    | => permHelper(1, [1, 2, 3], perm)| => permHelper(2, [1, 2, 3], perm)|
# i != len(array) - 1                  | i != len(array) - 1              | i == len(array) - 1              |
# -------------------------------------|----------------------------------|----------------------------------|
# j = 0                                | j = 1                            | perm.append([1, 2, 3])           |
# swap 0, 0 => [1, 2, 3]               | swap 1, 1 => [1, 2, 3]           | 
# permHelper(1, [1, 2, 3], perm)       | permHelper(2, [1, 2, 3], perm)   |
# -------------------------------------|----------------------------------|                                       
# j = 1                                | j = 2                            |
# swap 0, 1 => [2, 1, 3]               | swap 1, 2 => [1, 3, 2]           |
# permHelper(1, [2, 1, 3], perm)       | permHelper(2, [1, 3, 2], perm)   |
# -------------------------------------|----------------------------------|  
# j = 2                                |                                         
# swap 0, 2 => [3, 2, 1]               |            
# permHelper(1, [3, 2, 1], perm)       |   
# -------------------------------------|

# ==============
# Time and Space
# ==============
# O(n*n!) time | O(n*n!) space

def getPermutations(array):
    permutations = []
	permutationsHelper(0, array, permutations)
	return permutations

def permutationsHelper(i, array, permutations):
	if i == len(array) - 1:
		permutations.append(array[:])
	else:
		# swap elements from i
		for j in range(i, len(array)):
			swap(array, i, j)
			permutationsHelper(i + 1, array, permutations)
			swap(array, i, j)
			
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]