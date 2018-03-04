# https://leetcode.com/problems/read-n-characters-given-read4

"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it
returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that
reads n characters from the file.

Note:
The read function will only be called once for each test case.
"""

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

        res = 0
        while True:
            buf4 = [''] * 4
            count4 = read4(buf4)
            for i in range(min(count4, n-res)):
                buf[res] = buf4[i]
                res += 1
            if count4 < 4 or res == n:
                return res

