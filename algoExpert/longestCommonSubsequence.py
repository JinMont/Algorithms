# Before dive in
# ==============
# 1)Our goal is to construct the longest common subsequence (LCS)
# 2) Make a two dimensional array
# 3) first column and row are made with an empty string
# 4)    "" x k y k z p w
# 5) ""  ` ` ` ` ` ` ` ` <= find LCS of the empty string in this row and the element in each column
#     z  ` ` ` ` ` z z z <= means LCS of Z or empty string in Z versus XKYKZPW is Z
#     x  ` x x x x x x x 
#     v  ` x x x x x x x
#     v  ` x x x x x x x
#     y  ` x x xy xy xy xy xy
#     z  ` x x xy xy xyz xyz xyz
#     w  ` x x xy xy xyz xyz xyzw <= answer
# 6) empty strings work as base cases so we can initialize the first and the first column
# 7) when we don't have LCS we copy the left or the top box
# 8) when we have a LCS like in the z row 
#  a) we look the box in [i-1][j-1] (diagonal) and concatenate with lcs in the box
# 9) when both boxes have same length like the case of the row x we just pick arbitrary x or z

# Time
# ====
# 1) when you have two strings
# 2) the maximum LCS is the minimum of length of the two strings
# 3) N * M * min(N, M) 
#  a) multiplying length of each array and the number of concatenation

# Space
# =====
# 1) Space is same as O(NM * min(n, M)) 
#  a) we have n*m size array and in each index we have the min(N, M) number of elements
# 2) we can improve the space complexity by using only last two rows since we only need them to compute
# 3) reduce the space complexity to only O(NM)
# 4) we have O(NM * min(N, M)) because we concantenate the LCS
# 5) instead we can use a boolean to check whether we have LCS and have a pointer for the previous LCS

def longestCommonSubsequence(str1, str2): 
    lcs = [[[] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):
			if str2[i - 1] == str1[j - 1]:
				lcs[i][j] = lcs[i - 1][j - 1] + [str2[i - 1]]
			else:
				lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key = len) # compare their length
	return lcs[-1][-1] 