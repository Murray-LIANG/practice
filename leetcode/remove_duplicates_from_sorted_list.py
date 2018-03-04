# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next is None:
            return str(self.val)
        return '{} -> {}'.format(self.val, self.next)

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        i = head

        while i:
            j = i.next
            while j and j.val == i.val:
                j = j.next

            i.next = j
            i = j

        return head

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
