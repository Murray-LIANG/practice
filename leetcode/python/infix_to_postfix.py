class Solution(object):

    def infixToPostfix(self, s):
        """
        :type s: str
        :rtype: str
        """
        priority = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}
        result = []

        ops = []

        for c in s:
            if c not in priority.keys():
                result.append(c)
            else:
                if c == '(' or not ops or priority[c] > priority[ops[-1]]:
                    ops.append(c)
                else:
                    while ops and priority[c] <= priority[ops[-1]]:
                        t = ops.pop()
                        if t != '(':
                            result.append(t)
                        else:
                            break
                    if c != ')':
                        ops.append(c)
            print('result: {}'.format(result))
            print('ops: {}'.format(ops))

        while ops:
            result.append(ops.pop())


        return ''.join(result)


if __name__ == '__main__':
    datas = [
        ('a+b*c+(d*e+f)*g', 'abc*+de*f+g*+'),
    ]

    for i, (s, expected) in enumerate(datas, 1):
        print('>>> Test #{} <<<'.format(i))
        print('Infix: {}.'.format(s))
        result = Solution().infixToPostfix(s)
        print('Result: {}. Expected: {}. {}.'.format(
            result, expected,
            'PASS' if result==expected else 'FAIL'))
