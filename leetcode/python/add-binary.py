# https://leetcode.com/problems/add-binary

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        i, j = len(a) - 1, len(b) - 1

        res = []
        carry = 0
        while i >= 0 or j >= 0:
            a_num = int(a[i]) if i >= 0 else 0
            b_num = int(b[j]) if j >= 0 else 0
            carry, m = divmod(a_num + b_num + carry, 2)
            res.append(m)
            i -= 1
            j -= 1

        if carry > 0:
            res.append(carry)

        return ''.join([str(i) for i in reversed(res)])


print(Solution().addBinary('11', '1'))
print(Solution().addBinary('0', '0'))
print(Solution().addBinary('1', '111'))
