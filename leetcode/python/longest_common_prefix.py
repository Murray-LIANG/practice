class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''
        
        to_break = False
        for i in range(len(strs[0])):
            print('i: ', i)
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:
                    print('hit')
                    to_break = True
                    break
            if to_break:
                break
        else:
            i = len(strs[0])

        #if i == 0:
        #    return ''
        #else:
        #    return strs[0][0:i]
        return strs[0][0:i]


if __name__ == '__main__':
    datas = [
        (['a', 'ab', 'abc'], 'a'),
        (['', 'ab', 'abc'], ''),
        (['abc', 'ef', 'abc'], ''),
        (['abcd', 'a', 'abc'], 'a'),
        ([''], ''),
    ]

    for strs, expected in datas:
        result = Solution().longestCommonPrefix(strs)
        print('strs: {}. Longest common prefix: {}. Expected: {}'.format(
            strs, result, expected == result))
