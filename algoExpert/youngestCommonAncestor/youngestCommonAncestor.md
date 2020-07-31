# youngest common ancestor
## Flow
### 1. find the depth of two descendants
### 2. compare the depth of both and increase the height of 
###    the lower element up to the height of the higher descendant
### 3, loop until both descendants find the common ancestor
### 4. each loop makes the descendants find their ancestors until 
###    both have the same ancestor

## Time and Space
### Time: O(d) time where d is the depth of the ancestral tree
### - Since the descedants need to move only d times to find the common ancestor
###  - I think if the tree is not balanced it takes O(n) where n is the number of descendants and if it is balanced it takes O(log(n)) where n is the number of descendants in the tree. 
### Space: O(1) space
### - need only constant space
