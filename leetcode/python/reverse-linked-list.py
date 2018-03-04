# https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode('d')
        current = head

        while current:
            curr_next = current.next
            current.next = dummy.next
            dummy.next = current
            current = curr_next

        return dummy.next

    def reverseList_2(self, head):

        dummy = ListNode('d')

        def _recursive(head, dummy):
            current = head
            if not current:
                return
            head = head.next
            current.next = dummy.next
            dummy.next = current
            _recursive(head, dummy)

        _recursive(head, dummy)
        return dummy.next


def print_link(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(' -> '.join(str(each) for each in res))


n5 = ListNode(5)
n4 = ListNode(4)
n4.next = n5
n3 = ListNode(3)
n3.next = n4
n2 = ListNode(2)
n2.next = n3
n1 = ListNode(1)
n1.next = n2
print_link(Solution().reverseList(n1))
# print_link(Solution().reverseList_2(n1))
