package main

import "fmt"

/*
https://leetcode.com/problems/maximum-depth-of-binary-tree/
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left := maxDepth(root.Left)
	right := maxDepth(root.Right)
	if left > right {
		return left + 1
	} else {
		return right + 1
	}
}

func main() {
	n1, n2, n3, n4, n5 := TreeNode{Val: 1}, TreeNode{Val: 2}, TreeNode{Val: 3}, TreeNode{Val: 4}, TreeNode{Val: 5}
	n1.Left = &n2
	n1.Right = &n3
	n2.Right = &n4
	n4.Right = &n5
	fmt.Println(maxDepth(&n1))
}
