package main

/*
https://leetcode.com/problems/odd-even-linked-list
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func oddEvenList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	odd, even, evenStart := head, head.Next, head.Next

	for even != nil && even.Next != nil {
		odd.Next = even.Next
		even.Next = even.Next.Next
		odd = odd.Next
		even = even.Next
	}
	odd.Next = evenStart
	return head
}

func main() {

}
