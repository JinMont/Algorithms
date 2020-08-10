# Group Anagram

# ==============
# Before dive in
# ==============
# 1) Anangram
#  a) a group of words that are formed with same letters
#  ex) cinema, iceman

# ====
# Time
# ====
# sorting each word takes nlog(n) time and there are w words so wnlog(n) time

# =====
# Space
# =====
# O(wn) since there are w words and the length of a word is at most, n

def groupAnagrams(words):
	# Use hash
	anagrams = {}
	for word in words:
		sortedWord = "".join(sorted(word))
		# if there is sortedWord key in the hash
		if sortedWord in anagrams:
			anagrams[sortedWord].append(word)
		# if there is not sortedWord key make one
		else:
			anagrams[sortedWord] = [word]
	return list(anagrams.values())