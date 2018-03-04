package main

import (
	"fmt"
)

/*
https://leetcode.com/problems/symmetric-tree
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}

	var helper func(left *TreeNode, right *TreeNode) bool
	helper = func(left *TreeNode, right *TreeNode) bool {
		if left == nil || right == nil {
			return left == right
		}

		if left.Val == right.Val {
			return helper(left.Left, right.Right) && helper(left.Right, right.Left)
		}
		return false
	}
	return helper(root.Left, root.Right)
}

func main() {
}
