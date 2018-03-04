class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # w(i,j) is the most water between i and j. We need to calculate
        # w(0,len).
        # v(i,j) is the water area between i and j.
        # w(i,j) = max{w(i,j-1),
        #              max{v(k,j), i<=k<=j-1},
        #              w(i+1,j),
        #              max{v(i,k), i+1<=k<=j}}
        #        = max{w(i,j-1),
        #              w(i+1,j),
        #              v(i,j)}
        # Here, we could use DP to solve this problem.
        # But we could use greedy here.
        # w(i,j-1) and w(i+1,j) overlap most of part.
        # Let assume height[i] > height[j], there are two cases:
        # 1. v(i,j) contains the most water. Then w(i,j) = v(i,j).
        # 2. v(i,j) is not the most water container. Then w(i,j-1) or w(i+1,j)
        # contains the most water. The most import is that w(i+1,j) ==
        # w(i+1,j-1). The proof is that if j is the boundary of the most water
        # container. Because height[i] > height[j], v(i,j) would contain the
        # most water then. So j is not the boundary.
        # Thus the conclusion is that
        # w(i,j) = max( v(i,j),
        #               w(i,j-1) if height[i] > height[j]
        #               or w(i+1, j) otherwise )
        # The complexity is O(n).
        result = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] > height[j]:
                result = max(result, (j - i) * height[j])
                j -= 1
            else:
                result = max(result, (j - i) * height[i])
                i += 1
        return result


if __name__ == '__main__':
    datas = [
        ([1], 0),
        ([], 0),
        ([1,2,3,4,5,6,7], 12),
    ]

    for height, expected in datas:
        water = Solution().maxArea(height)
        print('Height: {}. Most water: {}. Expected: {}'.format(
            height, water, expected == water))

