# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times

"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it
returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that
reads n characters from the file.

Note:
The read function may be called multiple times.
"""


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        # for read
        #self._cache = []

        # for read_2
        from collections import deque
        self._cache = deque([])

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        while len(self._cache) < n:
            buf4 = [''] * 4
            count4 = read4(buf4)
            self._cache += buf4[:count4]
            if count4 < 4:
                break

        res = min(len(self._cache), n)
        for i in range(res):
            buf[i] = self._cache[i]
        self._cache = self._cache[res:]
        return res


    def read_2(self, buf, n):
        res = 0
        while res < n and self._cache:
            buf[res] = self._cache.popleft()
            res += 1

        while res < n:
            buf_4 = [''] * 4
            count_4 = read4(buf_4)
            copy_count = min(count_4, n-res)
            for i in range(copy_count):
                buf[res] = buf_4[i]
                res += 1

            for i in range(copy_count, count_4):
                self._cache.append(buf_4[i])

            if count_4 < 4:
                break
        return res

