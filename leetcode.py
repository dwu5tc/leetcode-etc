class Solution(object):
	# 476 number complement (easy)
	# given a positive int, output its complement (flip the bits of its binary representation)
	def findComplement(self, num):
		# flip num first (incl leading zeros)
		# then get last n bits by & 11...1 (n ones)
		return ~num & ((1<<num.bit_length())-1)

	# 500 keyboard row (easy)
	# given list of words, return words that can be typed using letters on one row of the american keyboard
	def findWords(self, words):
		solution = []
		top_row = ("q", "w", "e", "r", "t", "y", "u", "i", "o", "p")
		mid_row = ("a", "s", "d", "f", "g", "h", "j", "k", "l")
		bot_row = ("z", "x", "c", "v", "b", "n", "m")
		for word in words:
			is_valid = True
			# which row possible based on first letter
			if word[0].lower() in top_row:
				# check other letters
				for i in range(1, len(word)):
					if word[i].lower() not in top_row:
						is_valid = False
						break;
				if is_valid: 
					solution.append(word)
			elif word[0].lower() in mid_row:
				for i in range(1, len(word)):
					if word[i].lower() not in mid_row:
						is_valid = False
						break;
				if is_valid:
					solution.append(word)

			else:
				for i in range(1, len(word)):
					if word[i].lower() not in bot_row:
						is_valid = False
						break;
				if is_valid:
					solution.append(word)
			return solution
	# using a set would be faster

	# someone else's regex solution
	def findWords(self, words):
		return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words) 

	# 515 find largest value in each tree row (med)
	def largestValues(self, root):
		solution = []
		curr_row = [root]
		while len(curr_row) > 0: 
			new_row = []
			row_max = None
			for node in curr_row:
				if node:
					new_row.extend([node.left, node.right])
					if node.val > row_max: 
						row_max = node.val
			if row_max is not None:
				solution.append(row_max)
			curr_row = new_row
		return solution

	# someone else's solution
	def largestValues(self, root):
		maxes = []
		row = [root]
		while any(row):
			maxes.append(max(node.val for node in row))
			row = [kid for node in row for kid in (node.left, node.right) if kid]
		return maxes

	# someone else's divide and conquer solution
	def largestValues(self, root):
		if not root:
			return []
		left = self.largestValues(root.left)
		right = self.largestValues(root.right)
		return [root.val] + map(max, left, right)

	# 2 add two numbers (med)
	# given 2 linked lists representing 2 numbers, return a linked list representing their sum
	# list nodes are the digits; digits stored in reverse order
	
	# definition for singly-linked list
	# class ListNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None 
	def addTwoNumbers(self, l1, l2):
			carry = 0;
			solution = curr = ListNode(0)
			while l1 or l2 or carry:
				sum = carry
				if l1:
					sum += l1.val
					l1 = l1.next
				if l2:
					sum += l2.val
					l2 = l2.next
				carry = sum/10
				sum %= 10
				curr.next = curr = ListNode(sum)
			return solution.next

	# 20 valid parentheses (easy)
	# given string of parentheses, return if brackets open/close in correct order
	def isValid(self, s):
		opening = ["(", "[", "{"]
		closing = [")", "]", "}"]
		parentheses = []
		for i in range(0, len(s)): 
			if len(parentheses) == 0 and s[i] in closing:
				return False
			if s[i] in opening:
				parentheses.append(s[i])
			else:
				if parentheses[-1] != opening[closing.index(s[i])]:
					return False
				else:
					del parentheses[-1]
		return len(parentheses) == 0
	# using a dict would be faster

	# 15 3 sum (med)
	# given array of integers, return all triplets which give sum 0
	def threeSum(self, nums):
		solution = []
		nums.sort()
		# left = b index
		# right = c index
		# a+b+c == 0; b+c == -a
		left = right = 0
		for i in range(len(nums)-2):
			if i > 0 and nums[i] == nums[i-1]:
				continue
			left, right = i+1, len(nums)-1
			while left < right: 
				# b+c < -a; increase b 
				if nums[left]+nums[right] < -nums[i]: 
					left += 1
				# b+c > -a; decrease c
				elif nums[left]+nums[right] > -nums[i]:
					right -=1
				else:
					solution.append([nums[i], nums[left], nums[right]])
					# increase/decrease indexes to find new integers
					while left < right and nums[left] == nums[left+1]:
						left += 1
					while left < right and nums[right] == nums[right-1]:
						right -= 1
					# update b/c
					left += 1
					right -= 1
		return solution

	# 463 island perimeter (easy)
	# given an 2d int array where 1 = land, 0 = water, return the perimeter of the island
	def islandPerimeter(self, grid):
		islands = neighbors = 0
		for i in range (0, len(grid)):
			for j in range (0, len(grid[i])):
				if grid[i][j] == 1:
					islands += 1
					if j < len(grid[i])-1 and grid[i][j+1] == 1:
						neighbors += 1
					if i < len(grid)-1 and grid[i+1][j] == 1:
						neighbors += 1
		return (islands*4)-(neighbors*2)

	# 226 invert binary tree (easy)
	# recursive solution
	def invertTree(self, root):
		if root:
			root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
		return root

	# iterative solution
	def invertTree(self, root):
		stack = [root]
		while stack:
			curr = stack.pop()
			if curr:
				curr.left, curr.right = curr.right, curr.left
				stack.extend([curr.left, curr.right])
		return root

	# 206 reverse linked list
	# smh at this garbage recursive solution 
	# do better smh
	def reverseList(self, head):
		if head:
			if head.next:
				tail = head
				new_head = self.reverse(head, head.next)
				tail.next = None
				return new_head
			else:
				return head
		
	def reverse(self, new_tail, new_head):
		if new_head.next:
			temp = new_head.next
			new_head.next = new_tail
			return self.reverse(new_head, temp)
		else:
			new_head.next = new_tail
			return new_head

	# iterative solution



