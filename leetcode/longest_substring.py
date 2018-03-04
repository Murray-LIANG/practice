class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        DP:
        Assume s[start ... i-1] is the longest substring without repeating
        characters that ends with s[i-1].
        Then consider the i-th char in s, that is s[i]. Let's say s[k+1 ... i]
        is the longest substring ending with s[i]. k is the rightest location
        that s[i] is found in s. So we need some structure to store the
        information of k for each char.
        To keep max length we need to compare current max length with the
        length of s[k ... i], that is (i-k+1).
        """

        max_len = 0
        k = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                k = max(k, d[s[i]] + 1)

            max_len = max(max_len, i - k + 1)
            d[s[i]] = i

        return max_len


if __name__ == '__main__':
    test_datas = [
        'abcabcbb',
        'bbbbb',
        'pwwkew',
        '',
        'a',
        'au',
        'abcba',
        'abcabcde'
    ]

    for data in test_datas:
        print('Testing data: {}'.format(data))
        max_len = Solution().lengthOfLongestSubstring(data)
        print('Max length: {}'.format(max_len))
        #print('Max string: {}'.format(max_s))


