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
				carry = sum / 10
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
		# a+b+c == 0; b+c == -a
		left = right = 0
		# iterate through
		# i = a index
		for i in range(len(nums) - 2):
			# skip repeated integers
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			# left = b index
			# right = c index
			left, right = i + 1, len(nums) - 1
			while left < right: 
				# b+c < -a; increase b 
				if nums[left] + nums[right] < -nums[i]: 
					left += 1
				# b+c > -a; decrease c
				elif nums[left] + nums[right] > -nums[i]:
					right -= 1
				else:
					solution.append([nums[i], nums[left], nums[right]])
					# skip repeated integers
					while left < right and nums[left] == nums[left + 1]:
						left += 1
					while left < right and nums[right] == nums[right - 1]:
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
					if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
						neighbors += 1
					if i < len(grid) - 1 and grid[i + 1][j] == 1:
						neighbors += 1
		return (islands * 4) - (neighbors * 2)


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
	# smh at this garbage recursive solution 
	# do better smh

	# iterative solution
	# ...

	# 21 merge two sorted lists (easy)
	def mergeTwoLists(self, l1, l2):
	    if not l1 or not l2:
	        return l1 or l2
	    
	    if l1.val > l2.val:
	        l1, l2 = l2, l1
	    
	    head = l1
	    while l1 and l2:
	        if l1.next:
	            if l1.next.val <= l2.val:
	                l1 = l1.next
	            else:
	                temp = l1.next
	                l1.next = l2
	                l1, l2 = l2, temp
	        else:
	            l1.next = l2
	            break
	    return head


	# 35 search insert position (easy)
	def searchInsert(self, nums, target):
	    mid = len(nums) // 2
	    if nums[mid] == target:
	        return mid
	    
	    if target < nums[mid]:
	        if mid <= 0 or nums[mid - 1] < target:
	            return mid
	        return self.searchInsert(nums[0:mid], target)
	    else:
	        if mid >= len(nums) - 1 or nums[mid + 1] > target:
	            return mid + 1
	        return mid + 1 + self.searchInsert(nums[mid + 1:], target)


	# 53 maximum subarray (easy)
	def maxSubArray(self, nums):
	    if not nums:
	        return 
	    curr_sum = max_sum = nums[0]
	    
	    for x in range(1, len(nums)):
	        if nums[x] > curr_sum:
	            curr_sum = max(nums[x], curr_sum + nums[x])
	        else:
	            curr_sum += nums[x]
	        if curr_sum > max_sum:
	            max_sum = curr_sum  
	    return max_sum


	# 112 path sum 3 (easy)        
	def pathSum(self, root, sum):
	    if not root:
	        return 0
	    return self.pathSumHelper(root, sum, [])

	def pathSumHelper(self, root, sum, sums):
	    count = 0
	    sums.append(0)
	    for i in range(len(sums)):
	        sums[i] += root.val
	        if sums[i] == sum:
	            count += 1
	    if root.left:
	        count += self.pathSumHelper(root.left, sum, sums[:])
	    if root.right:
	        count += self.pathSumHelper(root.right, sum, sums[:])
	    return count


	# 113 path sum 3 ii (med)
	def pathSum(self, root, sum):
	    if not root:
	        return []
	    sum -= root.val;
	    paths = []
	    if not root.left and not root.right:
	        if sum == 0:
	            return [paths + [root.val]]
	    if root.left:
	        paths_left = self.pathSum(root.left, sum)
	        if len(paths_left) > 0:
	            paths += [[root.val] + path for path in paths_left]
	    if root.right:
	        paths_right = self.pathSum(root.right, sum)
	        if len(paths_right) > 0:
	            paths += [[root.val] + path for path in paths_right]
	    return paths


	# 128 longest consecutive sequence (hard)
	class Node(object):
	    def __init__(self, x):
	        self.val = x
	        self.next = None
	        self.prev = None

	class Solution(object):
	    def longestConsecutive(self, nums):
	        """
	        :type nums: List[int]
	        :rtype: int
	        """
	        dict = {}
	        for num in nums:
	            node = Node(num)
	            dict[num] = node
	            if num - 1 in dict:
	                dict[num - 1].next = node
	                node.prev = dict[num - 1]
	            if num + 1 in dict:
	                dict[num].next = dict[num + 1]
	                dict[num + 1].prev = dict[num]
	        max_count = 0
	        keys = dict.keys()
	        for key in keys:
	            if key not in dict:
	                continue
	            start = dict[key]
	            count = 0
	            node = start
	            while (node):
	                del dict[node.val]
	                node = node.prev
	                count += 1
	            if start.next:
	                node = start.next
	                while (node):
	                    del dict[node.val]
	                    node = node.next
	                    count += 1
	            max_count = max(max_count, count)
	        return max_count
	# so stupid... could've just used a set and iteratively check for adjacent numbers 

	# dcp 143
	def pivot_partition(x, lst):
	    l, r = 0, len(lst) - 1
	    while (l < r):
	        if lst[l] < x :
	            l += 1
	            continue
	        if lst[r] > x:
	            r -= 1
	            continue
	        if lst[l] > x:
	            lst[l], lst[r] = lst[r], lst[l]
	            r -= 1
	        elif lst[l] == x:
	            i = 1
	            while lst[l + i] == x:
	                if l + i < r:
	                    i += 1
	                else:
	                  return lst
	            if lst[l + i] < x:
	              lst[l], lst[l + i] = lst[l + i], lst[l]
	              l += 1
	            else:
	              lst[l + i], lst[r] = lst[r], lst[l + i]
	              r -= 1
	    return lst

	# dcp 144 
	def nearest_larger_num(i, lst):
	    l, r = i - 1, i + 1
	    while l > -1 and r < len(lst):
	        if lst[l] > lst[i] or lst[r] > lst[i]:
	            return l if lst[l] > lst[r] else r
	        l += 1
	        r += 1   
	    return None

	# assuming lst is preprocessed
	def nearest_larger_num_constant(i, lst):



