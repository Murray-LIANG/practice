class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def is_valid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        tmp_set = {s}
        while True:
            valid = filter(is_valid, tmp_set)
            if valid:
                return list(valid)
            tmp_set = {s[:i] + s[i+1:] for s in tmp_set for i in range(len(s))}


test_data = {
    '()())()': ['()()()', '(())()'],
    '(a)())()': ['(a)()()', '(a())()'],
    ')(': []
}

for data, expected in test_data.items():
    print('*' * 60)
    print('Inputting s: {}'.format(data))
    result = Solution().removeInvalidParentheses(data)
    print('Outputting: {}'.format(result))
    print('Expected: {}'.format(set(result)==set(expected)))


