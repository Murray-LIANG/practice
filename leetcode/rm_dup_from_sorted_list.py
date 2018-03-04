# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
        
        tail = head

        i = head
        while i is not None:            
            j = i.next
            while j is not None and i.val == j.val:
                j = j.next

            if i.next == j:
                if i != head:
                    tail.next = i
                tail = i
            elif i == head:
                head = j
            else:
                tail.next = j
            
            i = j

        return head


def printList(head):
    curr = head
    out_str = ""
    while curr is not None:
        out_str += "%s >>> " %(curr.val)
        curr = curr.next
    print(out_str + "None\n")



if __name__ == "__main__":

    head = None
    curr = None
    for i in [1,2,2,3]:
        node = ListNode(i)
        if head is None:
            head = node
            curr = node
        else:
            curr.next = node
            curr = node

    printList(head)

    new = Solution().deleteDuplicates(head)

    printList(new)