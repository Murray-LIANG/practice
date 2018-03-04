package main

import "fmt"

type ListNode struct {
	Val int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	dummyHead := &ListNode{0, nil}
	dummyHead.Next = head
	head, pre, i := dummyHead, dummyHead, dummyHead.Next
	for i != nil {
		j := i.Next
		if j != nil {
			i.Next = j.Next
			pre.Next = j
			j.Next = i
			pre = i
			i = i.Next
		} else {
			break
		}
	}
	return head.Next
}

func genTestList(num int) *ListNode {
	head := &ListNode{-1, nil}
	tmp := head
	for i := 0; i < num; i++ {
		tmp.Next = &ListNode{i, nil}
		tmp = tmp.Next
	}
	return head.Next
}

func printList(head *ListNode) {
	for head != nil {
		fmt.Print(head.Val, "->")
		head = head.Next
	}
	fmt.Println("END")
}

func main() {
	for i := 0; i < 5; i++ {
		fmt.Println("Round #", i)
		head := genTestList(i)
		fmt.Print("Test Data:")
		printList(head)
		result := swapPairs(head)
		fmt.Print("After swap:")
		printList(result)
		fmt.Println("===================")
	}
}
