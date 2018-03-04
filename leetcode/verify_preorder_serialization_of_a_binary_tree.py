class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        if not preorder:
            return True
        stack = []

        for c in preorder.split(','):
            if c != '#':
                stack.append(c)
            else:
                # Pop two char from the stack till the last is not '#'
                while stack and stack[-1] == '#':
                    stack.pop()
                    if not stack:
                        return False
                    stack.pop()

                stack.append(c)

        print(stack)
        return len(stack) == 1 and stack[0] == '#'

if __name__ == '__main__':
    datas = [
        ('', True),
        ('9', False),
        ('#', True),
        ('#,9', False),
        ('#,#', False),
        ('1,#,#', True),
        ('1,#,#,9', False),
        ('9,3,4,#,#,1,#,#,2,#,6,#,#', True),
    ]

    for i, (preorder, expected) in enumerate(datas, 1):
        print('>>> Test #{} <<<'.format(i))
        print('Preorder: {}.'.format(preorder))
        result = Solution().isValidSerialization(preorder)
        print('Result: {}. Expected: {}. {}.'.format(
            result, expected,
            'PASS' if result==expected else 'FAIL'))
