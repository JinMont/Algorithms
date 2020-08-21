# Max Sum Increasing Subsequence

# ==================
# Before dive in
# ==================
# 1) Solve this problem using dymamic programming
# 2) store the sum of increasing subsequence of each element in the variable 'sums'
# 3) store the index of the sum added to each element in the variable 'sequences'
# 4) Example:
#    array => [8, 12, 2, 3, 15, 5, 7]
#    sums => [8, 20, 2, 5, 23, 10, 17]
#    sequences => [ None, 0, None, 2, 1,  ,  ]
#    By following the index stored in the variable 'sequences' you can also build the sequence
#    None <= 0 <= 1 <= 4
#            8    12   15
# 5) return the max sum and the increasing subsequence of the array 
#  a) [23, [8, 12, 15]]

def maxSumIncreasingSubsequence(array):
	sequences = [None for x in array]
	sums = [num for num in array]
	maxSumIdx = 0
	for i in range(len(array)):
		currentNum = array[i]
		for j in range(0, i):
			otherNum = array[j]
			# this is strictly increasing
			# depends on the interviewer it can include equal as well
			if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
				sums[i] = sums[j] + currentNum
				sequences[i] = j
		#w when sum of index i is equal or greater than sum of previous max sum index
		if sums[i] >= sums[maxSumIdx]:
			maxSumIdx = i
	return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]

# buildSequence gets the sequence steps by following index stored in sequences variable
def buildSequence(array, sequences, currentIdx):
	sequence = []
	while currentIdx is not None:
		sequence.append(array[currentIdx])
		currentIdx = sequences[currentIdx]
	return list(reversed(sequence))