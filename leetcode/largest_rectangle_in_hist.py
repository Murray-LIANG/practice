class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        """
        stack = []

        max_area = 0
        i = 0
        while i < len(heights):
            if not stack or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                current = stack[-1]
                stack.pop()
                left = stack[-1] if stack else -1
                right = i
                max_area = max(max_area, heights[current] * (right - left - 1))

        while stack:
            current = stack[-1]
            stack.pop()
            left = stack[-1] if stack else -1
            right = i
            max_area = max(max_area, heights[current] * (right - left - 1))

        return max_area
        """

        # Append 0 to heights.
        heights.append(0)
        stack = []

        max_area = 0
        i = 0
        while i < len(heights):
            if not stack or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                current = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                max_area = max(max_area, heights[current] * (right - left - 1))

        return max_area


if __name__ == '__main__':
    data = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([6, 2, 5, 4, 5, 1, 6], 12),
        ([1], 1),
        ([1, 2, 3], 4),
        ([3, 2, 1], 4),
        ([0], 0),
        ([], 0),
    ]

    for heights, expected in data:
        message = 'Heights: {}.'.format(heights)
        result = Solution().largestRectangleArea(heights)
        print(message + ' Result: {}. Expected: {}'.format(result,
                                                           result==expected))
