"""
https://leetcode.com/problems/find-k-closest-elements

There are several solutions for this problem.

Solution 1: Use a heap of size k, iterate all numbers in the array, and put
abs(number-x) to the heap, every time the heap size reaches k, pop one out.
The time complexity of this solution is nlog(k).

Solution 2: Binary search. Do some conversion first.
This problem need us to find the number of index I, that
x - arr[I] <= arr[I+k] - x
2*x <= arr[I] + arr[I+k]

Due to the arr is increasing, arr[I] + arr[I+k] is increasing. So we are asked
to search the lower bound of I of which 2*x <= arr[I] + arr[I+k]
The time complexity is O(logn)
"""


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left, right = 0, len(arr) - 1 - k
        while left < right:
            mid = (left+right)/2
            if arr[mid] + arr[mid+k] < 2*x:
                left = mid + 1
            else:
                right = mid
        if arr[right] + arr[right+k] >= 2*x:
            return arr[right:right+k]
        return []
