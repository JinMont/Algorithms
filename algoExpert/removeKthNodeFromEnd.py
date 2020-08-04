# Remove Kth Node From End

# ==============
# Before dive in
# ==============
# 1) Singly linked list
#  a) no prev attribute in a node
# 2) how to know a node is at kth from the end
#  a) use two pointers and one pointer goes before like a scout

# ====
# FLOW
# ====
# 1) Use two pointers such as, first and second
# 2) second pointer is k nodes ahead of first pointer 
# 3) want to know the previous node of the kth node
#    since we want to connect the next of the previous node of kth 
#    to the next node of kth when we remove the node on the kth from the end
#    (since this is singly linked we only have value and next attributes)
# 4) for example, when k is 4 
#    0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> NULL
#                           first kth           second              
#                                  1    2    3    4
#    first stops at the node right before the kth and second stops at the last node

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
	counter = 1
    second = head
	first = head
	
	# 1) you want the counter to be less or equal to k
	# 2) since second needs to be k steps ahead of first
	while counter <= k:
		second = second.next
		counter += 1
	
	# 1) when second is already at None
	# 2) 0 -> 1 -> 2 -> 3 -> None
	#  first                second
	if second == None:
		head.value = head.next.value
		head.next = head.next.next
		return
	
	# 1) first pointer will be on the node right before the node that we want to remove
	# 2) we want the first to be on there so we can connect the pre first node with the node after kth
	# 3) second will stop at the last node when second.next is not none
	while second.next != None:
		second = second.next
		first = first.next
	
	# 1) we want the first on the node right before the kth node that we want to remove
	# 2) in that case we can connect the linked list after removing the kth node
	first.next = first.next.next