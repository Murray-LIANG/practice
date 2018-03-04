class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        count_a, count_l = 0, 0
        for c in s:
            if c == 'L':
                count_l += 1
            else:
                count_l = 0
                if c == 'A':
                    count_a += 1
                    if count_a > 1:
                        return False
            if count_l > 2:
                return False
        return True


datas = (
    ('PPALLP', True),
    ('PPALLL', False),
    ('LALL', True))

for (data, expected) in datas:
    print('>>> Test data: {}'.format(data))
    result = Solution().checkRecord(data)
    print('>>> Reward: {}'.format(result))
    print('>>> Pass: {}'.format(result == expected))
