# https://leetcode.com/problems/group-anagrams

from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for s in strs:
            res[''.join(sorted(s))].append(s)

        return res.values()


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
