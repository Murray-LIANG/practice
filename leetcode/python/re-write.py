def two_sum(nums, target):
	cache = {}
	for i in range(len(nums)):
		if (target - nums[i]) in cache:
			return (cache[target-nums[i]], i)
		else:
			cache[nums[i]] = i
	return (-1, -1)


def two_sum_sorted(nums, target):
	i, j = 0, len(nums)-1
	while i < j:
		if nums[i] + nums[j] == target:
			return (i+1, j+1)
		elif nums[i] + nums[j] < target:
			i += 1
		else:
			j -= 1
	return (-1, -1)


def three_sum(nums):
	
	def _two_sum(numbers, target):
		res = []
		i, j = 0, len(numbers)-1
		while i < j:
			tmp = [numbers[i], numbers[j]]
			if sum(tmp) == target:
				res.append(tmp)
				while i < j and numbers[i] == numbers[i+1]:
					i += 1
				while i < j and numbers[j] == numbers[j-1]:
					j -= 1
			elif sum(tmp) < target:
				i += 1
			else:
				j -= 1
		return res
	
	nums.sort()
	res = []
	for i in range(len(nums)):
		if i > 0 and nums[i] == nums[i-1]:
			continue
		two_sum_res = _two_sum(nums[i+1:], target-nums[i])
		if two_sum_res:
			res += [[nums[i]] + each for each in two_sum_res]
	return res


def roman_to_int(s):
	map = {'M': 1000, 'D': 500, 'C':100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

	res = 0
	for i in range(len(s)):
		j = i + 1
		if j == len(s) or map[s[i]] >= map[s[j]]:
			res += map[s[i]]
		else:
			res -= map[s[i]]
	return res


def letter_combination(digits):
	map = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
	
	res = []
	for digit in digits:
		res = [each+ch for each in res for ch in map[digit]]
	return res


def is_valid_parentheses(s):
	stack = []
	map = {')': '(', ']': '[', '}': '{'}
	for ch in s:
		if ch in map.values():
			stack.append(ch)
		else:
			if stack and stack[-1] == map[ch]:
				stack = stack[:-1]
			else:
				return False
	return not stack
		    

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __cmp__(self, other):
		return cmp(self.val, other.val)

import heapq
def merge_k_lists(lists):
	dummy = ListNode('h')

	heap = []
	for l in lists:
		if l:
			heapq.heappush(heap, l)
	
	current = dummy
	while heap:
		heap_top = heapq.heappop(heap)
		current.next = heap_top
		current = current.next
		
		if heap_top.next:
			heapq.heappush(heap, heap_top.next)
	return dummy.next


def merge_k_lists_2(lists):
	if not lists:
		return None
	if len(lists) == 1:
		return lists[0]
	
	first_half = merge_k_lists_2(lists[:len(lists)/2])
	second_half = merge_k_lists_2(lists[len(lists)/2:])
	return merge_2_lists(first_half, second_half)


def merge_2_lists(head_a, head_b):
	# Each list is sorted.
	dummy = ListNode('head')
	current = dummy
	
	pointer_a = head_a
	pointer_b = head_b
	while pointer_a and pointer_b:
		if pointer_a.val < pointer_b.val:
			current.next = pointer_a
			pointer_a = pointer_a.next
		else:
			current.next = pointer_b
			pointer_b = pointer_b.next
		current = current.next
	rest = pointer_a if pointer_a else pointer_b
	if rest:
		current.next = rest
	return dummy.next


def remove_duplicates(nums):
	if not nums:
		return 0

	res = 1
	current = num[0]
	for num in nums[1:]:
		if num != current:
			nums[res] = num
			res += 1
			current = num
	return res


def str_str(haystack, needle):
	for i in range(len(haystack)-len(needle)+1):
		if haystack[i:].startswith(needle):
			return i
	return -1


def search_in_rotated_sorted_array(nums, target):
	left, right = 0, len(nums)-1

	while left <= right:
		mid = (left+right)/2
		if nums[mid] == target:
			return mid
		if nums[mid] >= nums[left]:
			if nums[left] <= target < nums[mid]:
				right = mid - 1
			else:
				left = mid + 1
		else:
			if nums[mid] < target <= nums[right]:
				left = mid + 1
			else:
				right = mid - 1
	return -1
	

def count_and_say(n):
	
	def _helper(s):
		# s is not empty string
		s += '$'
		res = ''
		i, count = 1, 1
		while i < len(s):
			if s[i] == s[i-1]:
				count += 1
			else:
				res += str(count) + s[i-1]
				count = 1
			i += 1
		return res
	
	res = '1'
	for _ in range(n-1):
		res = _helper(res)
	return res


def multiply(num1, num2):
	def _helper(num1, digit):
		res = 0
		digit = int(digit)
		for index, ch in enumerate(num1[::-1]):
			res += int(ch) * digit * (10 ** index)
		return res

	if not all([num1, num2]):
		return '0'
	
	res = 0
	for index, ch in enumerate(num2[::-1]):
		res += _helper(num1, ch) * (10 ** index)
	return str(res)
		

from collections import defaultdict
def group_anagrams(strs):
	res = defaultdict(list)
	for s in strs:
		res[''.join(sorted(s))].append(s)
	return res.values()


class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e


def merge(intervals):
	if not intervals:
		return []
	
	intervals.sort(key=lambda i: i.start)
	res = [intervals[0]]
	for interval in intervals[1:]:
		if interval.start <= res[-1].end:
			res[-1].end = max(interval.end, res[-1].end)
		else:
			res.append(interval)
	return res
		

def add_binary(a, b):
	i, j = len(a)-1, len(b)-1
	res = ''
	carry = 0
	while i >= 0 or j >= 0:
		num_a = int(a[i]) if i >= 0 else 0
		num_b = int(b[j]) if j >= 0 else 0
		carry, tmp = divmod(num_a + num_b + carry, 2)
		res += str(tmp)
		i -= 1
		j -= 1
	
	if carry > 0:
		res += str(carry)
	return res[::-1]












		
