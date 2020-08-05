# Powerset (Iterative and Recursive ways)

# ====
# Flow
# ====
# 1) start with an empty set within an subset list
# 2) loop through all the element in array
#  a) add an element on its turn into the subsets in the powerset list

# ====
# Time
# ====
# 1) add n elements in 2^n subsets therefore O(2^n * n)

# =====
# Space
# =====
# 1) O(2^n * n) since there are 2^n subsets and n elements in array

"""
source:
The power set of a set with n elements contains 2^n elements
https://mathedia.com/the-power-set-of-a-set-with-n-elements-contains-2n-elements/

Proof
base case: n = 0
The set which contains 0 elements is the empty set ∅={ }.

Its power set contains 1 element (1 = 20), namely the empty set: 𝑃(∅)={∅}={{ }}.

Iinductive step: A(n) => A(n+1)
Let 𝑀𝑛+1 be a set with n+1 elements. 𝑒1, 𝑒2, … 𝑒𝑛, 𝑒𝑛+1.

It hast the subset 𝑀𝑛 with n elements 𝑒1, 𝑒2, … 𝑒𝑛.

𝑃(𝑀𝑛) has 2𝑛 elements (assumption), namely the 2𝑛 subsets of 𝑀𝑛: 𝑇1, 𝑇2,… 𝑇2𝑛.

They are the subsets of 𝑀𝑛 that implies that they are subsets of 𝑀𝑛+1 so they are elements of 𝑃(𝑀𝑛+1).

Additionally contains 𝑃(𝑀𝑛+1) the subsets ofon 𝑀𝑛+1 that contain the element 𝑒𝑛+1

Those can be constructed by joining 𝑇𝑖𝑖∈{1…2𝑛} with 𝑒𝑛+1

Each subset 𝑇𝑖 adds one element: 𝑒𝑛+1. 𝑇𝑖‘=𝑇𝑖∪𝑒𝑛+1. The number of subsets doubles.

We have:
𝑃(𝑀𝑛+1)={𝑇1, 𝑇2,… 𝑇2𝑛, 𝑇1‘, 𝑇2‘,… 𝑇′2𝑛}
The power set has 2𝑛+2𝑛=2⋅2𝑛=2𝑛+1 elements.

q.e.d.
"""

# Iterative
def powerset(array):
	subsets = [[]]
	# n elements
	for ele in array:
		# every ele for loop we are doubling the subsets
		# therefore 2^n subsets
		for i in range(len(subsets)):
			currentSubset = subsets[i]
			subsets.append(currentSubset + [ele])
	return subsets

# Recursive
def powerset(array, idx=None):
    if idx is None:
		idx = len(array) - 1
	if idx < 0:
		return [[]]
	ele = array[idx]
	subsets = powerset(array, idx - 1)
	for i in range(len(subsets)):
		currentSubset = subsets[i]
		subsets.append(currentSubset + [ele])
	return subsets
