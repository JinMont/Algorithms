# Min Rewards

# ==============
# Before dive in
# ==============
# 1) Rules
#  a) every student gets a grade and a reward
#  b) if they have a higher grade than students next to them they get higher rewards
# 2) find the minimum rewards necessary to give out that can satisfy the rules
# 3) only give out positive integers for grade and reward (if this isn't stated you can ask to clarify)
# 4) every student has a different grade
# 5) the order of the grade array matters so you can't sort the array of the grade
# Example)
#  a) [8, 4, 2, 1, 3, 6, 7, 9, 5] <= grade
#  b) [4, 3, 2, 1, 2, 3, 4, 5, 1] <= reward | minimum rewards used = 25

# ====
# Time
# ====
# 1) O(n^2)

# =====
# Space
# =====
# 1) O(n) 

def minRewards(scores):
	rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
		j = i - 1
		if scores[j] < scores[i]:
			rewards[i] = rewards[j] + 1
		else:
			while j >= 0 and scores[j] > scores[j+1]:
				# pick rewards for j in between its original reward and addition of 1 to reward of j+1
				# if rewards[j] is already bigger than rewards[j+1] + 1
				# it can just use its own reward (prob, incremented from previous lower grades)
				rewards[j] = max(rewards[j], rewards[j+1] + 1)
				j -= 1
	return sum(rewards)