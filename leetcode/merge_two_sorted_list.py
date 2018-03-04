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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        i = l1
        j = l2
        head = ListNode('head')
        k = head

        while i and j:
            if i.val <= j.val:
                k.next = i
                i = i.next
            else:
                k.next = j
                j = j.next
            k = k.next

        while i:
            k.next = i
            i = i.next
            k = k.next

        while j:
            k.next = j
            j = j.next
            k = k.next

        return head.next


if __name__ == '__main__':
    n1 = ListNode('1')
    n2 = ListNode('2')
    n3 = ListNode('3')
    n4 = ListNode('4')
    n5 = ListNode('5')
    n6 = ListNode('6')

    n1.next = n3
    n3.next = n5
    n2.next = n4
    n4.next = n6

    datas = [
        (n1, n2, '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL'),
    ]

    for l1, l2, expected in datas:
        print('l1: {}. l2: {}.'.format(l1, l2))
        result = Solution().mergeTwoLists(l1, l2)
        print('l1: {}. l2: {}. Result: {}. Expected: {}'.format(
            l1, l2, result, expected == str(result)))
