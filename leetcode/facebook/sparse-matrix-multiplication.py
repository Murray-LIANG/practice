# https://leetcode.com/problems/sparse-matrix-multiplication

"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not A[0]:
            return []
        m = len(A)
        l = len(A[0])
        assert l == len(B)
        n = len(B[0])
        if n == 0:
            return []
        res = [[0]*n for _ in range(m)]

        for i in range(m):
            for k in range(l):
                if A[i][k] != 0:
                    for j in range(n):
                        if B[k][j] != 0:
                            res[i][j] += A[i][k] * B[k][j]
        return res
