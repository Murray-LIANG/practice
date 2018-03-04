# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k

"""
Given an array nums and a target value k, find the maximum length of a subarray
that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed
integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
"""


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Let s[i] is the sum of nums[0] ... nums[i] inclusively.
        Then the sum of subarray from i to j is s[j] - s[i-1].
        For each j, check s[j]-s[i-1] == k for each 0<=i<=j.
        If exist, then j - (i-1) is the length of subarray.
        Store calculated s in a dict for quick find.

        For special case i == 0, s[-1] = 0.
        """

        s = []
        for num in nums:
            s.append(num + (s[-1] if s else 0))

        res = 0
        map = {0: -1}
        for i in range(len(nums)):
            if (s[i] - k) in map:
                res = max(res, i - map[s[i] - k])
            if s[i] not in map:
                map[s[i]] = i
        return res

    def maxSubArrayLen_2(self, nums, k):
        """

        :param nums:
        :param k:
        :return:

        s[i] = sum( [0...i) )
        s[j] = sum( [0...j) )
        s[j] - s[i] = sum( [i...j-1] )
        The count of number is (j-1-i+1) = j-i
        So, s[j] - s[i] = k, s[j] - k = s[i], if we have cache[s[i]] = i, then
        we could calculate the count j-i, and record the maximal one.
        """

        s = [0]
        for num in nums:
            s.append(s[-1] + num)

        res = 0
        cache = {0: 0}
        for j in range(1, len(nums) + 1):
            if s[j] - k in cache:
                res = max(res, j - cache[s[j] - k])

            if s[j] not in cache:
                cache[s[j]] = j
        return res
