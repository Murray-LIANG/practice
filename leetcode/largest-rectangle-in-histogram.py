# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        Use a stack to store the ascending heights. For each new height, pop
        all the heights in stack higher than the new one, and calculate the
        area with the popped height as the lowest height of area.
        """
        stack = []
        res = 0
        heights.append(0)  # Sentinel
        for index, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                res = max(res, heights[top] * (index - 1 -
                                               (stack[-1] if stack else -1)))
            stack.append(index)
        return res

print(Solution().largestRectangleArea([3]))
