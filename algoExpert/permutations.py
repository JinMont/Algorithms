# Permutations 

# =======
# Example
# =======
# array = [1, 2, 3]
# 
# => permHelper([1, 2, 3], [], perm)| => permHelper([2, 3], [1], perm)| => permHelper([3], [1, 2], perm)|
# i = 0                             | i = 0                           | i = 0                           |
# ----------------------------------|---------------------------------|---------------------------------|  
# newArray = [2, 3]                 | newArray = [] + [3]             | newArray = [] + []              |
# newPerm = [] + [1]                | newPerm = [1] + [2]             | newPerm = [1, 2] + [3]          |
# permHelper([2, 3], [1], perm)     | permHelper([3], [1, 2], perm)   | permHelper([], [1, 2, 3], perm) |
# ----------------------------------|---------------------------------|---------------------------------|
# => permHelper([1, 2, 3], [], perm)|
# i = 1                             | 
# ----------------------------------|
# newArray = [1] + [3] = [1, 3]     |
# newPerm = [] + [2] = [2]          |
# permHelper([1, 3], [2], perm)     |
# ----------------------------------|
# => permHelper([1, 2, 3], [], perm)|
# i = 2                             |
# ----------------------------------|
# newArray = [1, 2] + []            |
# newPerm = [] + [3]                |
# permHelper([1, 2], [3], perm)     |

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