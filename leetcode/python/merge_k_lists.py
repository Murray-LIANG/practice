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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if len(lists) == 1:
            return lists[0]

        left = self.mergeKLists(lists[:len(lists)/2])
        right = self.mergeKLists(lists[len(lists)/2:])

        return self.mergeTwoLists(left, right)

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
    n7 = ListNode('7')
    n8 = ListNode('8')
    n9 = ListNode('9')

    n1.next = n5
    n5.next = n7
    n2.next = n4
    n4.next = n9
    n3.next = n6
    n6.next = n8

    datas = [
        (n1, n2, n3, '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> NULL'),
    ]

    for l1, l2, l3, expected in datas:
        print('l1: {}. l2: {}. l3: {}.'.format(l1, l2, l3))
        result = Solution().mergeKLists([l1, l2, l3])
        print('Result: {}. Expected: {}'.format(result, expected == str(result)))
