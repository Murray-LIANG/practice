package main

import (
	"math"
	"fmt"
)

/*
https://leetcode.com/problems/binary-tree-maximum-path-sum

For each node N in the tree, we could calculate the sum of the tree with N as
the root. And check the sum with the current max one to see whether it could be
the new max one. Then recursively, N's longer path (right or left) could be in
path of N's parent with max sum.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxPathSum(root *TreeNode) int {
	res := math.MinInt32
	var helper func(*TreeNode) int
	helper = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		sumLeft, sumRight := max(0, helper(node.Left)), max(0, helper(node.Right))
		sum := node.Val + sumLeft + sumRight
		res = max(res, sum)
		return node.Val + max(sumLeft, sumRight)
	}

	helper(root)
	return res
}

func main() {
	n1 := &TreeNode{1, nil, nil}
	n2 := &TreeNode{-2, nil, nil}
	n3 := &TreeNode{3, nil, nil}
	n4 := &TreeNode{4, nil, nil}
	n5 := &TreeNode{5, nil, nil}

	n3.Left = n2
	n3.Right = n5
	n5.Left = n1
	n5.Right = n4

	fmt.Println(maxPathSum(n3))
}
