class Solution(object):
    max_int_32 = 2**31-1
    min_int_32 = -2**31

    def valid_int(self, x):
        return 0 if x > self.max_int_32 or x < self.min_int_32 else x

    def reverse_v1(self, x):
        s = list(str(x))[1:] if x < 0 else list(str(x))
        for i in range(0, (0+len(s)-1)/2 + 1):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]

        result = int(''.join(s)) if s >= 0 else 0-int(''.join(s))
        return self.valid_int(result)


    def reverse_v2(self, x):
        if x > self.max_int_32 or x < self.min_int_32:
            return 0

        result = 0

        neg = False
        if x < 0:
            neg = True
            x = 0 - x

        while x:
            x, r = divmod(x, 10)
            result = result * 10 + r

        if neg == True:
            result = 0 - result

        return self.valid_int(result)

    reverse = reverse_v2


if __name__ == '__main__':
    test_datas = [
        0,
        100,
        123,
        1234,
        -10,
        -123,
        -1234,
        1534236469
    ]

    for data in test_datas:
        print('>>>>> Reverse {}'.format(data))
        print(Solution().reverse(data))
        print('')

