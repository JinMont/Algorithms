# Balanced Brackets

# ==============
# Before dive in 
# ==============
# 1) Possible unbalace
#  a) a closing bracket without a prior matching opening bracket
#  b) left with some opening brackets that haven't been matched

# 2) Which data strucutre?
#  a) should keep track of all the brackets and check an unbalace at each loop
# 3) Stack
#  a) characteristics of stack can help solving the problems and the question above

def balancedBrackets(string):
    openingBrackets = '([{'
	closingBrackets = ')]}'
	matchingBrackets = {")": "(", "]": "[", "}": "{"}
	stack = []
	for char in string:
		# check whether the char is an opening, closing bracket, or others
		if char in openingBrackets:
			stack.append(char)
		elif char in closingBrackets:
			# when char is a closing bracket stack should an opening bracket matching at its last index
			if len(stack) == 0:
				return False
			if matchingBrackets[char] == stack[-1]:
				stack.pop()
			else:
				return False
		else:
			continue
	
	return len(stack) == 0