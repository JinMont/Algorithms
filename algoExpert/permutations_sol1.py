# Permutations Solution 1

# =======
# Example
# =======
# array = [1, 2, 3]
# permHelper(array, currentPerm, perm)

# => permHelper([1, 2, 3], [], perm)| => permHelper([2, 3], [1], perm)| => permHelper([3], [1, 2], perm)| => permHelper([], [1, 2, 3], perm) 
# i = 0                             | i = 0                           | i = 0                           | perm.append([1, 2, 3])
# ----------------------------------|---------------------------------|---------------------------------|------------------------------------ 
# newArray = [2, 3]                 | newArray = [] + [3]             | newArray = [] + []              |
# newPerm = [] + [1]                | newPerm = [1] + [2]             | newPerm = [1, 2] + [3]          |
# permHelper([2, 3], [1], perm)     | permHelper([3], [1, 2], perm)   | permHelper([], [1, 2, 3], perm) |
# ----------------------------------|---------------------------------|---------------------------------|
# => permHelper([1, 2, 3], [], perm)| ====
# i = 1                             | FLOW
# ----------------------------------| ====
# newArray = [1] + [3] = [1, 3]     | 1) when there len(array) exists 
# newPerm = [] + [2] = [2]          |  a) make newArray and newPerm using for loop
# permHelper([1, 3], [2], perm)     |  b) each loop will make newPerm with new element added on the next index in newPerm
# ----------------------------------|  c) newPerm = currentPerm + [array[i]]
# => permHelper([1, 2, 3], [], perm)| 2) when there is not len(array) left add currentPerm to the list of permutations
# i = 2                             |
# ----------------------------------| ==============
# newArray = [1, 2] + []            | Time and Space
# newPerm = [] + [3]                | ==============
# permHelper([1, 2], [3], perm)     | 1) Upper Bound: O(n^2*n!) time | O(n*n!) space
#                                   | 2) Roughly: O(n*n!) time | O(n*n!) space

def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations
    
def permutationsHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
        
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            newPermutation = currentPermutation + [array[i]]
            permutationsHelper(newArray, newPermutation, permutations)