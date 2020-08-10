# Longest Palindromic Substring

# ==============
# Before Dive in
# ==============
# 1) understand the concept of Palindrome
#  a) [a a] is palindrome (even numbers)
#  b) [a b a] is palindrome (odd numbers)
# 2) lambda function in this case set an rule to compare the max

def longestPalindromicSubstring(string):
	currentLongest = [0, 1]
	for i in range(1, len(string)):
		odd = getLongestPalindromeFrom(string, i - 1, i + 1)
		even = getLongestPalindromeFrom(string, i - 1, i)
		longest = max(odd, even, key = lambda x: x[1] - x[0])
		currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
	return string[currentLongest[0]: currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		leftIdx -= 1
		rightIdx += 1
	# When the while loop break
	# left index - 1 and right index + 1 are index we want 
	# Since we are going to slice add left indx + 1( inclusive) and leave the right Idx as it is (exclusive)
	return [leftIdx + 1, rightIdx]