# Suffix Trie Construction

# ==============
# Before dive in
# ==============
# 1) Suffix trie is a tree like data structure that contains all possible suffixes 
# 2) In the suffix trie, a key in a hash table is pointing to another hash table
# 3) Root node is an empty dictionary 
# 4) 'bab' is not a suffix of 'babc'
#  a) It is a prefix so we should not find bab in the suffix trie
# Example) string = "babc"
#       [empty]
#       /  |  \
#      b   a   c
#     /|   |   |
#    c a   b   *
#    | |   |   
#    * b   c
#      |   |
#      c   *
#      |
#      *

# ====
# Flow
# ====
# 1) Let's look at the entire substring starting at the each index
# 2) the first suffix trie will be the entire string starting at the index 0
# 3) check whether the letter at the current index is already stored in the root's or parent's hashtable
#  a) if it is not stored, add the value to the trie
#  b) the added value point to an empty hash table
#  c) move on to the next letter
# 4) Repeat until there is not a substring left
# 5) Add the final node * that marks the end of the string 

# ======
# Search
# ======
# 1) Time
#  a) O(m) where m is the length of the string we are searching for
#  b) we just follow the each char of the string in the trie
# 2) Space
#  a) O(1)

# ======
# Create
# ======
# 1) Time
#  a) O(n^2) 
#  b) Interating all the possible suffixes and its characters
#  c) 'babc', 'abc', 'bc', 'c' in each we look at the characters as well
#  d) number of possible suffixes * number of characters in each suffix = n*n = n^2
#  e) you can build with O(n) time with Ukkonen's Algorithm
# 2) Space 
#  a) O(n^2) average and worst case
#  b) It can be O(n) when the characters of the string are same
#   i) 'ttttt'

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)
	# O(n^2) time | O(n^2) space
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
			self.insertSubstringStartingAt(i, string)
	
	def insertSubstringStartingAt(self, i, string):
		node = self.root
		for j in range(i, len(string)):
			letter = string[j]
			if letter not in node:
				# if there is not the letter add the letter in the root's hash table
				node[letter] = {}
				# the letter points to its own hash table
			node = node[letter]
		node[self.endSymbol] = True
		# at the end of the string, the last node's hash table contains the *
	
	# O(m) time | O(1) space
    def contains(self, string):
        node = self.root
		for letter in string:
			if letter not in node:
				return False
			node = node[letter]
		return self.endSymbol in node
		# the hash table of the last node contains * and its value is True