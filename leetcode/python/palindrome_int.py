class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # let x = 14741,
        # x     rest
        # 1474  1
        # 147   14
        # 14    147

        # let x = 147741,
        # x     rest
        # 14774 1
        # 1477  14
        # 147   147
        if x < 0 or (x !=0 and x % 10 == 0):
            return False

        rest = 0
        while x > rest:
            x, r = divmod(x, 10)
            rest = rest*10 + r

        return x == rest//10 or x == rest


if __name__ == '__main__':
    test_datas = {
        147741,
        14741,
        -1,
    }

    for data in test_datas:
        print('>>>>> Is {} palindromic?'.format(data))
        print(Solution().isPalindrome(data))
