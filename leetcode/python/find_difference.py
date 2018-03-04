class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        s, t = sorted(s), sorted(t)
        if s == t[:-1]:
            return t[-1]
        else:
            return [x[0] for x in zip(t, s) if x[0] != x[1]][0]

        Use XOR or similar.

        return chr(reduce(operator.xor, map(ord, s + t)))

        or 
        """
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

if __name__ == '__main__':
    datas = [
        ('abcde', 'abdcfe', 'f'),
    ]

    for i, (s, t, expected) in enumerate(datas):
        print('>>>>> Test {}'.format(i))
        print('s: {}. t: {}.'.format(s, t))
        result = Solution().findTheDifference(s, t)
        print('Result: {}. Expected: {}.'.format(
            result, result==expected))
