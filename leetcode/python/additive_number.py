class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        pass

    def isAdditive(self, num, i, j):
        # The first number a is with length i, the second number b with length
        # j.
        n = len(num)
        if i + j > n:
            return False
        elif i + j == n:
            return True

        a = int(num[:i])
        b = int(num[i:j])

        start = i + j
        while start < n:
            a, b = b, a + b
            str_b = str(b)
            start += len(str_b)
            if not num.startswith(str_b):
                return False
        return True

        
if __name__ == '__main__':
    datas = [
        ([], None),
        ([1], '1'),
        ([1,1,1], '1'),
        ([1,1,2], '1 -> 2'),
        ([1,2,3], '1 -> 2 -> 3'),
    ]

    for i, (nodes, expected) in enumerate(datas, 1):
        print('>>> Test #{} <<<'.format(i))
        print('nodes: {}.'.format(nodes))
        head = ListNode('dummy')
        i = head
        for node in nodes:
            t = ListNode(node)
            i.next = t
            i = i.next
        result = Solution().deleteDuplicates(head.next)
        print('Result: {}. Expected: {}. {}.'.format(
            result, expected,
            'PASS' if str(result)==str(expected) else 'FAIL'))
