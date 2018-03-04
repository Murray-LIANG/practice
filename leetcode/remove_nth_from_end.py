# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '{} -> {}'.format(self.val,
                                 str(self.next) if self.next is not None
                                 else 'NULL')

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        i = head
        for _ in range(n):
            i = i.next

        if i is None:
            return head.next

        j = head
        while i.next:
            i = i.next
            j = j.next

        j.next = j.next.next
        return head

if __name__ == '__main__':
    n1 = ListNode('1')
    n2 = ListNode('2')
    n1.next = n2
    n3 = ListNode('3')
    n2.next = n3

    n4 = ListNode('4')

    datas = [
        (n1, 0, '1 -> 2 -> 3 -> NULL'),
        #(n1, 1, '1 -> 2 -> NULL'),
        #(n1, 2, '1 -> 3 -> NULL'),
        #(n1, 3, '2 -> 3 -> NULL'),
        #(n1, 4, '1 -> 2 -> 3 -> NULL'),
        #(n4, 0, '4 -> NULL'),
        (n4, 1, 'None'),
    ]

    for head, n, expected in datas:
        result = Solution().removeNthFromEnd(head, n)
        print('head: {}. n: {}. Result: {}. Expected: {}'.format(
            head, n, result, expected == str(result)))
