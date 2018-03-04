class Solution(object):
    def longest_arround_i(self, s, i, j):
        if i != j and (j == len(s) or s[i] != s[j]):
            return i, i
        d = 0
        for x in range(1, min(i, len(s)-1-j) + 1):
            if s[i-x] != s[j+x]:
                break
            d = x
        return i-d, j+d

    def longestPalindrome(self, s):
        # s[j..i..k] is palindromic substring while i-j == k-i. For x =
        # 1...min(j, len(s)-k), if s[j-x] == s[k+x], then s[j-x..i..k+x] is
        # palindromic substring, else continue next i.
        # Need to run another round to check if s[j..ii+1..k] is palindromic
        # substring while i-j == k-i.

        if not s:
            return s

        max_len_s = 0
        max_len_e = 0
        for i in range(len(s)):
            s1, e1 = self.longest_arround_i(s, i, i)
            s2, e2 = self.longest_arround_i(s, i, i+1)
            if e1-s1 >= e2-s2 and e1-s1 >= max_len_e-max_len_s:
                max_len_s = s1
                max_len_e = e1
            elif e2-s2 > e1-s1 and e2-s2 >= max_len_e-max_len_s:
                max_len_s = s2
                max_len_e = e2

        return s[max_len_s: max_len_e+1]

if __name__ == '__main__':
    test_datas = [
        'aaaaaaa',
        'a',
        '',
        '  ',
        'abcbasfds',
        'sdfeabcba',
        'sdfabba',
        'sdfabbbaa',
        'abbaeeeeeee',
        'abbaefffe'
    ]

    for s in test_datas:
        print('>>>>> Calculate max palindromic substring for {}'.format(s))
        print(Solution().longestPalindrome(s))
        print('')
