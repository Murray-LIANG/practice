class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str

            1 2 3
        x     4 5
        =
              1 5
            1 0
          0 5
            1 2
          0 8
        0 4
       =0 5 5 3 5
        Consider that 123 with index [0, 1, 2] in num1, while 45 with index
        [0, 1] in num2, then 3 * 5 = 15, the result 15 affects to the index [3,
        4] in final result. It is easy to conclude that num1[i] * num2[j] will
        affect the value in index [i+j, i+j+1] in result.
        """
        len1 = len(num1)
        len2 = len(num2)

        result = [0] * (len1 + len2)
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                v1, v2 = divmod(mul + result[p2], 10)
                result[p1] += v1
                result[p2] = v2

        s = ''
        for i in result:
            if s or i != 0:
                s += str(i)

        return s if s else '0'

if __name__ == '__main__':
    datas = [
        ('123', '45', '5535'),
    ]

    for num1, num2, expected in datas:
        result = Solution().multiply(num1, num2)
        print('num1: {}. num2: {}. Result: {}. Expected: {}'.format(
            num1, num2, result, expected == result))
