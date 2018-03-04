package main

import (
	"math"
	"fmt"
)

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxToRoot(root *TreeNode, result *int) int {
	if root == nil {
		return 0
	}
	left := maxToRoot(root.Left, result)
	right := maxToRoot(root.Right, result)
	if left < 0 {
		left = 0
	}
	if right < 0 {
		right = 0
	}
	if left + right + root.Val > *result {
		*result = left + right + root.Val
	}
	root.Val += max(left, right)
	return root.Val
}

func maxPathSum(root *TreeNode) int {
	result := math.MinInt32
	maxToRoot(root, &result)
	return result
}

func main() {
	n9 := TreeNode{9, nil, nil}
	n10 := TreeNode{10, nil, nil}
	n5 := TreeNode{5, nil, nil}
	n7 := TreeNode{7, nil, nil}
	n2 := TreeNode{2, &n9, &n10}
	n3 := TreeNode{3, &n5, &n7}
	n1 := TreeNode{1, &n2, &n3}
	fmt.Println("Max path sum:", maxPathSum(&n1))
}
