class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        nums = [0] * (n + 1)

        nums[n-1] = 0 if s[-1] == '0' else 1
        nums[n] = 1

        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                continue
            nums[i] = nums[i + 1]
            if int(s[i : i + 2]) < 27:
                nums[i] += nums[i + 2]

        return nums[0]


if __name__ == '__main__':
    datas = [
        ('', 0),
        ('0', 0),
        ('10', 1),
        ('100', 0),
        ('130', 0),
        ('30', 0),
        ('12', 2),
        ('125', 3),
        ("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948", 589824)
    ]

    for i, (s, expected) in enumerate(datas, 1):
        print('>>>>> Test {}'.format(i))
        result = Solution().numDecodings(s)
        print('S: {}. Result: {}. Expected: {}.'.format(s, result,
                                                        result==expected))

