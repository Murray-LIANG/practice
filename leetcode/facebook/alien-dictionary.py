"""
https://leetcode.com/problems/alien-dictionary

There is a new alien language which uses the latin alphabet. However, the order
among letters are unknown to you. You receive a list of non-empty words from
the dictionary, where words are sorted lexicographically by the rules of this
new language. Derive the order of letters in this language.

Example 1:
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Example 2:
Given the following words in dictionary,

[
  "z",
  "x"
]
The correct order is: "zx".

Example 3:
Given the following words in dictionary,

[
  "z",
  "x",
  "z"
]
The order is invalid, so return "".

Note:
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the
given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str

        Topological sort
        """

        if not words:
            return ''

        from collections import defaultdict, deque
        res = []
        all_ch = set(''.join(words))
        degree = defaultdict(int)
        next_alpha = defaultdict(list)

        for i in range(len(words) - 1):
            word, next = words[i], words[i + 1]
            for j in range(min(len(word), len(next))):
                if word[j] != next[j]:
                    if next[j] not in next_alpha[word[j]]:
                        next_alpha[word[j]].append(next[j])
                        degree[next[j]] += 1
                    break

        queue = deque()

        for ch in all_ch:
            if degree[ch] == 0:
                queue.append(ch)

        while queue:
            first = queue.popleft()
            res.append(first)

            for next in next_alpha[first]:
                degree[next] -= 1
                if degree[next] == 0:
                    queue.append(next)

        if len(res) != len(all_ch):
            return ''
        return ''.join(res)


# print(Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
# print(Solution().alienOrder(["za","zb","ca","cb"]))
print(Solution().alienOrder(["wrt","wrf","er","ett","rftt","te"]))
