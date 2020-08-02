# Min Heap Construction

# ==============
# Before dive in
# ==============
# 1) Satisfy the heap property (this time, the min heap)
# 2) Current Node => i | Child One => 2i + 1 | Child Two => 2i + 2
# 3) Parent Node => floor((i - 1)/2)

# ==========
# Components
# ==========
# 1) Build Heap 
#  a) Heapify (Using Sift Down more time efficient than Sift Up)
#  b) compare every parent with its children
#  c) if the parent is swapped, compare again with its new children 
#  d) Sift Down until satisfies the heap property
# 2) Sift Down
#  a) use after popping the root element and the last element is at the root
#  b) swap with its smaller child until it satisfies the heap property
#  c) compare with child one (2i + 1) and child two (2i + 2)
# 3) Sift Up
#  a) a new element is inserted
#  b) compare the new element with its parent element
#  c) swap with its parent until it satisfies the heap property
#  d) compare with its parent (floor((i - 1)/2))
# 4) Insert
#  a) Insert the new element at the last
#  b) Use Sift Up
# 5) Remove
#  a) the root element switches its position with the last element
#  b) the element used to be the last is now at the first
#  c) swap with its smaller child until it satisfies the heap property

# ====
# Time 
# ====
# 1) Build Heap - O(n)
# 2) Sift Down - O(log(n))
# 3) Sift Down - O(log(n))

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

	# O(n) time | O(1) space
    def buildHeap(self, array):
		# len(array) - 1 is currentIdx of last element 
		# you want to subtract another 1 to calculate parentIdx
        firstParentIdx = ((len(array) - 1) -1) // 2
		# you want to make firstParentIdx + 1 since range will go up to before firstParentIdx
		for currentIdx in reversed(range(firstParentIdx + 1)):
			
			self.siftDown(currentIdx, len(array) - 1, array)
		return array
		
		# 1) find the first parent index
		# 2) loop through all the indexes equal or lower than the first parent index
		# 3) execute siftDown on each node
			
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
			if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap] < heap[currentIdx]:
				self.swap(currentIdx, idxToSwap, heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				break

		# 1) find the child one 
		# 2) while loop to check whether the current index has children
		# 3) if there is the child two then assign childTwoIdx
		# 4) if there is the child two and the child two is smaller than child one assign idxToSwap as childTwoIdx
        # 5) vice versa
		# 6) if the smallest child is smaller than the current node swap
		# 7) if they are swapped assign currentIdx as dxToSwap and childOneIdx with new index
    
	def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
		while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
			self.swap(currentIdx, parentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
		valueToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return valueToRemove

		# 1) swap the first node and the last node
		# 2) pop the last node, previously the first node
		# 3) siftDown the first node to satisfy the heap property

    def insert(self, value):
        self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)
		
	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]
