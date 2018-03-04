class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        mapping = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in mapping.values():
                stack.append(c)
            elif c in mapping.keys():
                if not stack or mapping[c] != stack.pop():
                    return False
            else:
                return False

        return stack == []


if __name__ == '__main__':
    datas = [
        ('()', True),
        (')', False),
        ('(', False),
        ('()[]', True),
        ('([])', True),
        ('([]', False),
    ]

    for pstr, expected in datas:
        result = Solution().isValid(pstr)
        print('pstr: {}. Result: {}. Expected: {}'.format(
            pstr, result, expected == result))
