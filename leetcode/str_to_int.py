class Solution(object):
    max_int_32 = 2**31-1
    min_int_32 = -2**31
    def valid_int(self, i):
        if i > self.max_int_32:
            return self.max_int_32
        elif i < self.min_int_32:
            return self.min_int_32
        else:
            return i

    def my_atoi_v1(self, s):
        s = s.strip()
        start = 0
        neg = False
        result = 0
        if start >= len(s):
            return result
        if s[start] in ('-', '+'):
            neg = s[start] == '-'
            start += 1

        for i in range(start, len(s)):
            if s[i] >= '0' and s[i] <= '9':
                result = result * 10 + int(s[i])
            else:
                break
            if not neg and result > self.max_int_32:
                result = self.max_int_32
                break
            elif neg and result > self.max_int_32 + 1:
                result = self.max_int_32 + 1
                break

        return 0 - result if neg else result


    myAtoi = my_atoi_v1


if __name__ == '__main__':
    test_datas = [
        ('', 0),
        ('   ', 0),
        (' 1  ', 1),
        ('1', 1),
        ('+1', 1),
        ('99999999999999', 2**31-1),
        ('-99999999999999', -2**31),
        (' 1 0 ', 1),
        (' a ', 0),
        ('a', 0),
    ]

    for data in test_datas:
        print('>>>>> String {} to int'.format(data[0]))
        i = Solution().myAtoi(data[0])
        print('Result: {}. Expected: {}.'.format(i, i == data[1]))

