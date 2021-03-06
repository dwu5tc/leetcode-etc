// 448 find all disappeared numbers (easy)
// given an array of int where 1 <= a[i] <= n (n = size of array) and some numbers appear >= 1, return an array with the missing numbers
// without extra space
var findDisappearedNumbers = function(nums) {
		var solution = [];
		// for each i, mark the nums[i] as negative (this method saves space)
		// at the end, if any nums[i] are positive, this means the value of the index, i, was missing from the original array
		nums.forEach(function(elem) {
				var index = Math.abs(elem) - 1;
				nums[index] = Math.abs(nums[index]) * -1;
		})
		// for each i, if nums[i] is positive, push the index, i, t
		for (let i = 0; i < nums.length; i++) {
				if (nums[i] > 0) { solution.push(i + 1); }
		}
		return solution;
};


// 617 merge 2 binary trees (easy)
// given 2 binary trees, return a new binary tree which merges them such that new nodes use either the NOT null node (non-overlap)
// or a new node where val = the sum of the original node vals
/**
 * definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
var mergeTrees = function(t1, t2) {
		if (t1 && t2) {
				const newNode = new TreeNode(t1.val + t2.val);
				newNode.left = mergeTrees(t1.left, t2.left);
				newNode.right = mergeTrees(t1.right, t2.right);
				return newNode;
		}
		return t1 || t2;
};


// 581 shortest unsorted continuous subarray (easy)
// given an int array, return the length of the one continuous subarray st by sorting it (ascending), the whole array will be sorted (ascending)
var findUnsortedSubarray = function(nums) {
	if (nums.length > 1) {
		// beg and end track the beginning and ending of the subarray
		var beg;
		var end;
		var min = nums[nums.length - 1]; 
		var max = nums[0];
		for (let i = 0, j = nums.length - 1; i < nums.length; i++, j--) {
			// sweep right to left to find min
			// check for new min each iteration
			min = Math.min(min, nums[j])
			// if value at j < min, beg should be updated b/c a new subarray as been found
			if (min < nums[j]) {
				beg = j;
			}
			// sweep left to right to find max
			// same logic as above
			max = Math.max(max, nums[i])
			if (max > nums[i]) {
				end = i;
			}
		}
		if (beg < end) {
			return end - beg + 1;
		}
		else {
			// already sorted
			return 0;
		}
	}
	// already sorted
	return 0;
}
// THIS O(N) SOLUTION TOOK ME WAY TOO LONG...


// 141 linked list cycle (easy)
// given a link list, return whether it contains a cycle
// without extra space
var hasCycle = function(head) {
	if (head) {
		var slow = head;
		var fast = head;
		while (slow.next && fast.next.next) {
			slow = slow.next;
			fast = fast.next.next;
			if (slow === fast) {
				return true;
			}
		}
		return false;
	}
	return false;
}


// 21 merge 2 sorted lists (easy)
// given 2 sorted linked lists, return the single merged list
// must splice the nodes of the original lists 
// recursive solution
var mergeTwoLists = function(l1, l2) {
	if (l1 && l2) {
		if (l1.val <== l2.val) {
			l1.next = mergeTwoLists(l1.next, l2);
			return l1;
		} 
		else {
			l2.next = mergeTwoLists(l1, l2.next);
			return l2;
		}
	}
	return l1 || l2;
}

// iterative solution
var mergeTwoLists = function(l1, l2) {
	// implement
}


// 543 diameter of a binary tree (easy)
// given a binary tree, return the length of the diameter of the tree
// diameter = longest path between any 2 nodes
var diameterOfBinaryTree = function(root) {
	if (root) {
		// calculate the diameter of the left/right subtrees, as well as the sum of the max depths of the left/right subtrees
		return Math.max(diameterOfBinaryTree(root.left), diameterOfBinaryTree(root.right), maxDepth(root.left) + maxDepth(root.right));
	}
	return 0;
}

var maxDepth = function(root) {
	if (root) {
		return Math.max(maxDepth(root.left) + 1, maxDepth(root.right) +1);
	}
	return 0;
}
// seems inefficient with redundant operations involved...???


// 169 majority element (easy)
// given array size n, return the majority element (appears more than n/2 times)
// assume non-empty array 
var majorityElement = function(nums) {
	// implement 
}


// 572 subtree of another tree
// given 2 binary trees, s and t, return whether s contains t 
// assume non-empty trees
var isSubtree = function(s, t) {
	if (!s) {
		return false;
	}
	else if (s.val === t.val) {
		return isSubtreeHelper(s, t) || isSubtree(s.left, t) || isSubtree(s.right, t);
	} 
	else {
		return isSubtree(s.left, t) || isSubtree(s.right, t);
	}
}

var isSubtreeHelper = function(s, t) {
	if (!s && !t) {
		return true;
	}
	else if (!s || !t || s.val !== t.val) {
		return false;
	}
	else {
		return isSubtreeHelper(s.left, t.left) && isSubtreeHelper(s.right, t.right);
	}
}
// THIS TOOK ME WAY TOO LONG TOO


var twoSum = (nums, target) => {
	// implement 
};

