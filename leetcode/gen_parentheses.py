class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def gen_parenthesis(s, x, y):
            if x <= 0 and y <= 0:
                result.append(s)
                return

            if x > 0:
                gen_parenthesis(s+'(', x-1, y)
            if y > x:
                gen_parenthesis(s+')', x, y-1)

        gen_parenthesis('', n, n)
        return result


if __name__ == '__main__':
    datas = [
        (3, ['((()))', '(()())', '(())()', '()(())', '()()()']),
    ]

    for n, expected in datas:
        result = Solution().generateParenthesis(n)
        print('n: {}. Result: {}. Expected: {}'.format(
            n, result, set(expected) == set(result)))
