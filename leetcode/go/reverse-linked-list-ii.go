package main

import "fmt"

/*
https://leetcode.com/problems/reverse-linked-list-ii
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseBetween(head *ListNode, m int, n int) *ListNode {
	dummy := &ListNode{-1, head} // Add a dummy node to the front.

	pre, start, current := dummy, dummy.Next, dummy.Next
	i := 1
	for ; i < m; i++ {
		pre = current
		current = current.Next
		start = current
	}

	for ; i < n; i++ {
		next := current.Next
		pre.Next = next
		current.Next = next.Next
		next.Next = start
		start = pre.Next
	}
	return dummy.Next
}

func toSlice(head *ListNode) []int {
	res := []int{}
	for node:=head; node != nil; node = node.Next {
		res = append(res, node.Val)
	}
	return res
}

func main() {

	n5 := &ListNode{5, nil}
	n4 := &ListNode{4, n5}
	n3 := &ListNode{3, n4}
	n2 := &ListNode{2, n3}
	n1 := &ListNode{1, n2}
	newHead := reverseBetween(n1, 2, 5)
	fmt.Println(toSlice(newHead))
}
