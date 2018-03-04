package main

import "fmt"

/*
https://leetcode.com/problems/same-tree
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	return helper(p, q)
}

func helper(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	if p != nil && q != nil && helper(p.Left, q.Left) && helper(p.Right, q.Right) {
		return p.Val == q.Val
	}
	return false
}

func main() {
	p1, p2, p3, p4, p5 := TreeNode{Val: 1}, TreeNode{Val: 2}, TreeNode{Val: 3}, TreeNode{Val: 4}, TreeNode{Val: 5}
	p1.Left = &p2
	p1.Right = &p3
	p2.Right = &p4
	p4.Right = &p5
	q1, q2, q3, q4, q5 := TreeNode{Val: 1}, TreeNode{Val: 2}, TreeNode{Val: 3}, TreeNode{Val: 4}, TreeNode{Val: 5}
	q1.Left = &q2
	q1.Right = &q3
	q2.Right = &q4
	q4.Right = &q5
	fmt.Println(isSameTree(&p1, &q1))

	p11 := TreeNode{Val: 11}
	fmt.Println(isSameTree(&p11, nil))
}
