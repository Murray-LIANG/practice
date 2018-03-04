"""
https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays

This problem need to calculate the max sum of 3 subarrays. Then split the nums
to 3 parts.
[0 ... i-1][i ... i+k-1][i+k ... n-1], while k <= i <= n-2k

Using DP, we need two arrays to store the below info:
1. Let index_left[j] denote the starting index from which the subarray having
the max sum in nums[0 ... j]. That is, say index_left[10] = 4, it means in
nums[0 ... 10], sum of nums[4, 4+k-1] is the max one between all the starting
indexes.
2. Like the left part, use index_right[j] to denote the starting index from
which the subarray having the max sum in nums[j ... n-1]. That is, say
index_right[10] = 6, it means in nums[10 ... n-1], sum of nums[6, 6+k-1] is the
max one between all the starting indexes.
"""


class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0 or n < 3 * k:
            return []

        def start_of(end_index):
            return end_index - k + 1

        def end_of(start_index):
            return start_index + k - 1

        # sums[i] = sum_of(nums[0:i]),
        # sums[j] - sums[i] = sum_of(nums[i:j]) = sum_of(nums[i ... j-1])
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)

        tmp_max = sums[k] - sums[0]
        index_left = [0] * (n - 2 * k)
        for j in range(k, n - 2 * k):
            start_j = start_of(j)
            if sums[j+1] - sums[start_j] > tmp_max:
                tmp_max = sums[j+1] - sums[start_j]
                index_left[j] = start_j
            else:
                index_left[j] = index_left[j - 1]

        tmp_max = sums[n] - sums[n - k]
        index_right = [n - k] * n
        for j in range(n - k - 1, 2 * k - 1, -1):
            end_j = end_of(j)
            if sums[end_j+1] - sums[j] >= tmp_max:  # Note the '='
                tmp_max = sums[end_j+1] - sums[j]
                index_right[j] = j
            else:
                index_right[j] = index_right[j + 1]

        max_3 = 0
        res = []
        for i in range(k, n - 2 * k + 1):
            left, right = index_left[i - 1], index_right[i + k]
            max_new = (sums[left + k] - sums[left] +
                       sums[i + k] - sums[i] +
                       sums[right + k] - sums[right])
            if max_new > max_3:
                res = [left, i, right]
                max_3 = max_new
        return res


print(Solution().maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2))
print(
Solution().maxSumOfThreeSubarrays([7, 13, 20, 19, 19, 2, 10, 1, 1, 19], 3))
