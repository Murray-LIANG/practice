# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        longest = ''

        for word in d:
            i = 0
            for ch in s:
                if i < len(word) and word[i] == ch:
                    i += 1
            if i == len(word):
                if len(word) > len(longest):
                    longest = word
                elif len(word) == len(longest) and word < longest:
                    longest = word

        return longest


print(Solution().findLongestWord('edcba', ['a', 'b', 'f']))