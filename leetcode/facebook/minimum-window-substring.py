"""
https://leetcode.com/problems/minimum-window-substring
"""

from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        Use two indexes - start and end, to indicate the start and end of the
        window we are checking whether all chars from t are contained. Besides,
        a dict named count_in_window is used to record the count info of each
        char between current window. The key is the char and the value is its
        count. The passive count means how many chars are still needed to
        contain the t (we need to move `end` forward to include more chars in).
        The negative count means how many times the chars are duplicated (we
        could move `start` forward to exclude the duplicated ones and let the
        window as minimal as we can).
        """

        start, end, counter = 0, 0, len(t)
        count_in_window = defaultdict(int)

        for ch in t:
            count_in_window[ch] += 1

        start_pos = window_size = len(s) + 1

        while end < len(s):
            if count_in_window[s[end]] > 0:
                counter -= 1
            count_in_window[s[end]] -= 1
            end += 1
            while counter == 0:
                if count_in_window[s[start]] == 0:
                    counter += 1
                if window_size > end - start:
                    window_size = end - start
                    start_pos = start
                count_in_window[s[start]] += 1
                start += 1

        return '' if start_pos == len(s) + 1 else s[start_pos:start_pos + window_size]

print(Solution().minWindow('ADOBECODEBANC', 'ABC'))
print(Solution().minWindow('a', 'aa'))
print(Solution().minWindow('a', 'a'))
