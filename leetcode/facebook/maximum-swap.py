"""
https://leetcode.com/problems/maximum-swap
"""


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        last_index = [-1] * 10
        num_lst = list(str(num))

        for i, n in enumerate(num_lst):
            last_index[int(n)] = i

        for i, n in enumerate(num_lst):
            for larger_digit in range(9, int(n), -1):
                if last_index[larger_digit] > i:
                    num_lst[i], num_lst[last_index[larger_digit]] = \
                        num_lst[last_index[larger_digit]], num_lst[i]
                    return int(''.join(num_lst))
        return num


