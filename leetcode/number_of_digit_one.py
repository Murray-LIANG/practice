class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        Consider the occurrence of 1 on the hundred position:
        4023 >>>              3100 ~ 3199, 2100 ~ 2199, 1100 ~ 1199, 100 ~ 199
        4123 >>> 4100 ~ 4123, 3100 ~ 3199, 2100 ~ 2199, 1100 ~ 1199, 100 ~ 199
        4223 >>> 4100 ~ 4199, 3100 ~ 3199, 2100 ~ 2199, 1100 ~ 1199, 100 ~ 199

        So let n = xyzhab, h is the number on the hundred position.
        if h == 0, Count = xyz * 100
        if h == 1, Count = xyz * 100 + ab + 1
        if h > 1,  Count = xyz * 100 + 100
        """

        result = 0
        # The position for hundred, thousand ...
        p = 1
        while p <= n:
            digit_on_p = (n / p) % 10
            result += n / p / 10 * p
            if digit_on_p == 1:
                result += n % p + 1
            elif digit_on_p > 1:
                result += p

            p *= 10

        return result


if __name__ == '__main__':
    datas = [
        (14023, 10237),
        (14123, 10381),
        (14223, 10577),
    ]

    for i, (num, expected) in enumerate(datas):
        print('>>>>> Test {}'.format(i))
        print('Number: {}.'.format(num))
        result = Solution().countDigitOne(num)
        print('Result: {}. Expected: {}.'.format(
            result, result==expected))
