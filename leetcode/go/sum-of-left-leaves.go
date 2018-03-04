package main

import "fmt"

/*
https://leetcode.com/problems/sum-of-left-leaves
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumOfLeftLeaves(root *TreeNode) int {
	if root == nil {
		return 0
	}
	res := 0
	if root.Left != nil {
		if root.Left.Left == nil && root.Left.Right == nil {
			res += root.Left.Val
		} else {
			res += sumOfLeftLeaves(root.Left)
		}
	}
	res += sumOfLeftLeaves(root.Right)
	return res
}

func main() {
	p1, p2, p3, p4, p5 := TreeNode{Val: 1}, TreeNode{Val: 2}, TreeNode{Val: 3}, TreeNode{Val: 4}, TreeNode{Val: 5}
	p1.Left = &p2
	p1.Right = &p3
	p3.Left = &p4
	p3.Right = &p5
	fmt.Println(sumOfLeftLeaves(&p1))
}
