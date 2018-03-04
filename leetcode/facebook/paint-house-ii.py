"""
https://leetcode.com/problems/paint-house-ii

There are a row of n houses, each house can be painted with one of the k
colors. The cost of painting each house with a certain color is different. You
have to paint all the houses such that no two adjacent houses have the same
color.

The cost of painting each house with a certain color is represented by a n x k
cost matrix. For example, costs[0][0] is the cost of painting house 0 with
color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?

"""


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        n, k = len(costs), len(costs[0])
        min1 = min2 = -1
        res = [0] * (k+1)

        for house in costs:
            pre_min1, pre_min2 = min1, min2
            min1 = min2 = -1
            tmp_res = [0] * (k+1)

            for color in range(k):
                tmp_res[color] = house[color] + (res[pre_min2]
                                                 if color == pre_min1
                                                 else res[pre_min1])

                if min1 == -1 or tmp_res[color] < tmp_res[min1]:
                    min2, min1 = min1, color
                elif min2 == -1 or tmp_res[color] < tmp_res[min2]:
                    min2 = color

            res = tmp_res
        return res[min1]
